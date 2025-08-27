import streamlit as st
import main  # import your predictor script

st.set_page_config(page_title="PinkShield • Landing", page_icon="🩺", layout="wide")

HERO_HTML = """
<style>
/* RESET STREAMLIT DEFAULT */
.block-container { padding-top: 1rem; }
header[tabindex="-1"], footer { visibility: hidden; height: 0; margin: 0; padding: 0; }

/* ---------- THEME COLORS ---------- */
:root {
  --bg: radial-gradient(1200px 700px at 10% -10%, rgba(135,206,250,.35), transparent 60%),
        radial-gradient(900px 600px at 110% 10%, rgba(255,182,193,.35), transparent 60%),
        linear-gradient(135deg, #0e0f14 0%, #0b0c10 100%);
  --glass: rgba(255,255,255,0.10);
  --glass-border: rgba(255,255,255,0.2);
  --glow: 0 0 40px rgba(56,189,248,.35), 0 0 80px rgba(56,189,248,.15);
}

body { background: var(--bg) fixed; }

.hero {
  position: relative;
  width: 100%;
  height: 480px;
  border-radius: 28px;
  overflow: hidden;
  background:
    radial-gradient(600px 300px at 20% 10%, rgba(56,189,248,.22), transparent 60%),
    radial-gradient(600px 300px at 80% 20%, rgba(255,182,193,.20), transparent 60%),
    linear-gradient(180deg, rgba(255,255,255,.04), rgba(255,255,255,0));
  border: 1px solid var(--glass-border);
  box-shadow: 0 20px 80px rgba(0,0,0,.45), var(--glow);
  backdrop-filter: blur(12px);
}

.grid {
  position: absolute; inset: 0;
  background-size: 60px 60px;
  background-image: linear-gradient(rgba(255,255,255,.06) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255,255,255,.06) 1px, transparent 1px);
  mask-image: radial-gradient(500px 250px at 40% 40%, black, transparent 65%);
}

.nav {
  position: absolute; top: 18px; left: 18px; right: 18px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 14px;
  border-radius: 16px; background: var(--glass);
  border: 1px solid var(--glass-border);
  backdrop-filter: blur(8px);
}
.pill {
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 500;
  color: #e5e7eb;
  border: 1px solid rgba(255,255,255,.25);
}
.cta {
  padding: 10px 20px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 700;
  border: 1px solid rgba(255,255,255,.25);
  color: white;
  background: linear-gradient(90deg, #38bdf8, #ec4899);
  text-decoration: none;
  box-shadow: var(--glow);
  transition: all 0.3s ease;
}
.cta:hover {
  transform: scale(1.05);
  background: linear-gradient(90deg, #0ea5e9, #db2777);
}

.stage {
  position: absolute; inset: 0; display: flex;
  flex-direction: column; align-items: center; justify-content: center;
  text-align: center;
}
.cluster {
  display: flex; align-items: center; gap: 18px;
  transform: translateY(10px);
  flex-direction: column;
}
.bag {
  width: 92px; height: 72px; border-radius: 18px 18px 8px 8px;
  background: linear-gradient(180deg, #38bdf8, #0284c7);
  box-shadow: inset 0 2px 6px rgba(255,255,255,.35), 0 14px 30px rgba(56,189,248,.35);
  position: relative;
  animation: bag-enter 1.2s cubic-bezier(.2,.8,.2,1) 0s both;
}
.bag:before {
  content: ""; position: absolute; left: 14px; right: 14px; top: -16px; height: 18px;
  background: linear-gradient(180deg, #bae6fd, #38bdf8);
  border-radius: 8px; box-shadow: 0 6px 14px rgba(56,189,248,.35);
}
.bag:after {
  content: ""; position: absolute; left: 0; right: 0; top: 28px; height: 6px;
  background: rgba(255,255,255,.35);
}
.lock {
  position: absolute; left: 50%; top: 36px; transform: translateX(-50%);
  width: 18px; height: 18px; border-radius: 6px;
  background: linear-gradient(180deg, #f9a8d4, #db2777);
  box-shadow: 0 6px 12px rgba(219,39,119,.35);
}

.brand {
  font-family: 'Orbitron', sans-serif;
  font-weight: 900;
  font-size: 50px;
  letter-spacing: 2px;
  color: #ffffff;
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.6),
               0 0 16px rgba(56,189,248,0.6);
  animation: brand-reveal 1.0s ease-out 1.75s both;
}
.tagline {
  font-size: 18px;
  color: #d1d5db;
  margin-top: 10px;
  max-width: 420px;
  line-height: 1.4;
  animation: brand-reveal 1.2s ease-out 2.3s both;
}

.statcard {
  position: absolute; right: 20px; bottom: 20px;
  padding: 14px; border-radius: 16px;
  background: var(--glass); border: 1px solid var(--glass-border);
  color: #e5e7eb; backdrop-filter: blur(8px);
  min-width: 240px; box-shadow: 0 12px 40px rgba(0,0,0,.35);
}
.bar { height: 8px; background: rgba(255,255,255,.15); border-radius: 999px; overflow: hidden; }
.bar > i { display: block; height: 100%; width: 0;
  background: linear-gradient(90deg, #ec4899, #38bdf8);
  animation: fill 1.2s ease-out 2.0s forwards;
}

@keyframes bag-enter {
  0% { transform: translateY(-40px) scale(.6) rotate(-8deg); opacity: 0; }
  60% { transform: translateY(4px) scale(1.04) rotate(0deg); opacity: 1; }
  100% { transform: translateY(0) scale(1) rotate(0deg); }
}
@keyframes brand-reveal { 0% { opacity: 0; } 100% { opacity: 1; } }
@keyframes fill { from { width: 0; } to { width: 92%; } }
</style>

<div class="hero">
  <div class="grid"></div>
  <div class="nav">
    <div class="pill">AI-Powered Breast Cancer Detector</div>
  </div>
  <div class="stage">
    <div class="cluster">
      <div class="bag"><div class="lock"></div></div>
      <div class="brand">PinkShield</div>
      <div class="tagline">Instantly analyze tumor characteristics using cutting-edge AI models trained on medical data.</div>
    </div>
  </div>
  <div class="statcard">
    <div style="font-weight:700; margin-bottom:6px;">Scanning Tumor Cells...</div>
    <div class="bar"><i></i></div>
    <div style="font-size:12px; opacity:.8; margin-top:8px;">Analyzing Nuclei Structure</div>
  </div>
</div>
"""

# Session state to track navigation
if "show_main" not in st.session_state:
    st.session_state.show_main = False

# Show landing if not yet clicked
if not st.session_state.show_main:
    st.components.v1.html(HERO_HTML, height=500)

    # 🚀 Start Button
    if st.button("🔍 Start Scan"):
        st.session_state.show_main = True
        st.rerun()
else:
    # 👉 load the predictor content from main.py
    main.main()
