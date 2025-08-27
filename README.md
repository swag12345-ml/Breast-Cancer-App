# Breast Cancer Detection App

**Live Demo:** [Explore the App Here](https://breast-cancer-app-ptavzznpynbl8dsvxgfxps.streamlit.app/)

---

##  Overview

This Streamlit-based web app predicts whether a breast tumor is **benign** or **malignant** using cytological measurements. The app is trained on the well-known Wisconsin Breast Cancer Dataset and offers an intuitive interface for users to input features and visualize results.

---

##  Features

- **Interactive Sidebar Sliders**  
  Adjust input features (e.g., radius, perimeter, smoothness) based on real dataset ranges.

- **Radar Chart Visualization**  
  See a visual representation of selected measurements for quick comparison.

- **Machine Learning Prediction**  
  Upload or select values to generate predictions—malignant or benign—on the spot.

- **Instant Feedback**  
  The app outputs predictions immediately, ideal for educational demonstrations or quick insights.

---

##  Dataset

Built on the **Wisconsin Breast Cancer Dataset** from the UCI Machine Learning Repository:

- Includes features like mean, SE, and worst for attributes such as radius, texture, area, smoothness, and more.
- Original data contains columns like `id`, `Unnamed: 32`, which are removed during preprocessing.
- Labels are mapped as:
  - `M → 1` (Malignant)
  - `B → 0` (Benign)
