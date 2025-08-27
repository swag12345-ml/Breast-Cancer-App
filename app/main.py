import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time


# ------------------ DATA LOADING ------------------
def get_clean_data():
    data = pd.read_csv("data/data.csv")
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    return data


# ------------------ SIDEBAR ------------------
def add_sidebar():
    st.sidebar.header("⚙️ Cell Nuclei Measurements")
    data = get_clean_data()

    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    input_dict = {}
    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )
    return input_dict


# ------------------ SCALE VALUES ------------------
def get_scaled_values(input_dict):
    data = get_clean_data()
    X = data.drop(['diagnosis'], axis=1)

    scaled_dict = {}
    for key, value in input_dict.items():
        max_val = X[key].max()
        min_val = X[key].min()
        scaled_value = (value - min_val) / (max_val - min_val)
        scaled_dict[key] = scaled_value
    return scaled_dict


# ------------------ RADAR CHART ------------------
# ------------------ RADAR CHART ------------------
def get_radar_chart(input_data):
    input_data = get_scaled_values(input_data)

    categories = [
        'Radius', 'Texture', 'Perimeter', 'Area',
        'Smoothness', 'Compactness',
        'Concavity', 'Concave Points',
        'Symmetry', 'Fractal Dimension'
    ]

    fig = go.Figure()
    neon_colors = ["#00ffff", "#ff00ff", "#00ff88"]

    traces = [
        ([input_data['radius_mean'], input_data['texture_mean'], input_data['perimeter_mean'],
          input_data['area_mean'], input_data['smoothness_mean'], input_data['compactness_mean'],
          input_data['concavity_mean'], input_data['concave points_mean'], input_data['symmetry_mean'],
          input_data['fractal_dimension_mean']], "Mean Value", neon_colors[0]),

        ([input_data['radius_se'], input_data['texture_se'], input_data['perimeter_se'], input_data['area_se'],
          input_data['smoothness_se'], input_data['compactness_se'], input_data['concavity_se'],
          input_data['concave points_se'], input_data['symmetry_se'], input_data['fractal_dimension_se']], "Standard Error", neon_colors[1]),

        ([input_data['radius_worst'], input_data['texture_worst'], input_data['perimeter_worst'],
          input_data['area_worst'], input_data['smoothness_worst'], input_data['compactness_worst'],
          input_data['concavity_worst'], input_data['concave points_worst'], input_data['symmetry_worst'],
          input_data['fractal_dimension_worst']], "Worst Value", neon_colors[2])
    ]

    for r, name, color in traces:
        fig.add_trace(go.Scatterpolar(
            r=r,
            theta=categories,
            fill='toself',
            name=name,
            line=dict(color=color, width=2),
            fillcolor=color.replace("#", "rgba(").replace("ff", "") if False else color,  # overwrite below
            opacity=0.4  # ✅ clean transparency
        ))

    # ✅ Clean dark radar style
    fig.update_layout(
        polar=dict(
            bgcolor="black",
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                gridcolor="gray",
                linecolor="gray",
                gridwidth=0.6,
                showline=True
            ),
            angularaxis=dict(
                gridcolor="gray",
                linecolor="gray"
            )
        ),
        showlegend=True,
        paper_bgcolor="black",
        font=dict(color="white", size=12),
        margin=dict(l=40, r=40, t=40, b=40)
    )

    return fig


# ------------------ PREDICTION ------------------
def add_predictions(input_data):
    model = pickle.load(open("model/model.pkl", "rb"))
    scaler = pickle.load(open("model/scaler.pkl", "rb"))

    input_array = np.array(list(input_data.values())).reshape(1, -1)
    input_array_scaled = scaler.transform(input_array)
    prediction = model.predict(input_array_scaled)

    st.subheader("🔬 Cell Cluster Prediction")
    st.write("The cell cluster is:")

    if prediction[0] == 0:
        st.success("🟢 Benign")
    else:
        st.error("🔴 Malignant")

    st.write("Probability of being benign:", model.predict_proba(input_array_scaled)[0][0])
    st.write("Probability of being malignant:", model.predict_proba(input_array_scaled)[0][1])
    st.caption("⚠️ This app can assist medical professionals but should not replace professional diagnosis.")


# ------------------ MAIN ------------------
def main():
    # 🚫 REMOVED st.set_page_config() → only in landing.py

    # ✅ Load CSS
    try:
        with open("assets/style.css", "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

    # Title animation
    st.markdown(
        """
        <div style="text-align:center; margin-bottom:20px;">
            <span class="stethoscope">🩺</span>
            <h1 class="title">Breast Cancer Predictor</h1>
            <div class="scan-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar. ")

    input_data = add_sidebar()

    # Cinematic loading effect
    with st.spinner("🩻 Scanning tissue sample..."):
        time.sleep(2.5)

    col1, col2 = st.columns([4, 1])

    with col1:
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart, use_container_width=True)

    with col2:
        add_predictions(input_data)


if __name__ == "__main__":
    main()
