import streamlit as st
import requests
from PIL import Image
import io
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="WCE Curated Colon Disease Detection ",
    page_icon="🧠",
    layout="wide",
)

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0f172a;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.subtitle {
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Prediction banner */
.prediction-banner {
    border-radius: 20px;
    padding: 22px;
    text-align: center;
    font-size: 22px;
    font-weight: 800;
    color: white;
    margin-bottom: 20px;
}

.metric-title {
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 38px;
    font-weight: bold;
    color: white;
}

.st-emotion-cache-vl2mil{
    margin-top:20px;
}

.status-good {
    color: #22c55e;
    font-size: 30px;
    font-weight: bold;
}

.status-bad {
    color: #ef4444;
    font-size: 30px;
    font-weight: bold;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("""
<div class="main-title">WCE Curated Colon Disease Detection</div>
<div class="subtitle">
Advanced Deep Learning WCE Curated Colon Disease Classification System
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Prediction History")

    if len(st.session_state.history) == 0:
        st.info("No predictions yet")

    else:
        for item in reversed(st.session_state.history[-10:]):
            color = "#22c55e" if item["label"] == "No Tumor" else "#ef4444"

            st.markdown(f"""
            <div style="
                background:#1e293b;
                padding:12px;
                border-radius:12px;
                margin-bottom:10px;
                border-left:5px solid {color};
            ">
                <div style="font-weight:bold; color:white;">
                    {item["label"]}
                </div>

                  Confidence : {item["confidence"]:.2f}%

                   At : {item["time"]}
            </div>
            """, unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    files = {
        "file": uploaded_file.getvalue()
    }

    with st.spinner("Analyzing MRI image..."):

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files=files
        )

    if response.status_code == 200:

        result = response.json()

        predicted_class = result["prediction"]
        confidence = result["confidence"]

        current_item = {
            "label": predicted_class,
            "confidence": confidence,
            "time": datetime.now().strftime("%H:%M:%S")
        }

        if (
                len(st.session_state.history) == 0
                or st.session_state.history[-1] != current_item
        ):
            st.session_state.history.append(current_item)

        if predicted_class == "No Tumor":
            banner_color = "linear-gradient(90deg,#84cc16,#ea580c)"
            status_text = "LOW RISK"
            status_class = "status-good"

        else:
            banner_color = "linear-gradient(90deg,#f59e0b,#dc2626)"
            status_text = "TUMOR DETECTED"
            status_class = "status-bad"

        left, right = st.columns([1.2, 1])

        with left:

            image = Image.open(io.BytesIO(uploaded_file.getvalue()))

            st.image(
                image,
                use_container_width=True
            )

        with right:

            # Prediction Banner
            st.markdown(f"""
            <div class="prediction-banner"
            style="background:{banner_color};">
                {predicted_class}
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    label=f"""Confidence of {predicted_class}""",
                    value=f"{confidence:.2f}%"
                )


            with col2:

                st.markdown("Risk Status")

                if predicted_class == "No Tumor":
                    st.success(status_text)
                else:
                    st.error(status_text)

            gauge_color = "green" if predicted_class == "No Tumor" else "red"

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=confidence,
                number={
                    "suffix": "%",
                    "font": {
                        "size": 48,
                        "color": "white"
                    }
                },
                gauge={
                    "axis": {
                        "range": [0, 100],
                        "tickcolor": "white"
                    },
                    "bar": {
                        "color": gauge_color
                    },
                    "bgcolor": "#1e293b",
                    "borderwidth": 2,
                    "bordercolor": "white",
                    "steps": [
                        {
                            "range": [0, 50],
                            "color": "#334155"
                        },
                        {
                            "range": [50, 80],
                            "color": "#475569"
                        },
                        {
                            "range": [80, 100],
                            "color": "#64748b"
                        }
                    ]
                }
            ))

            gauge.update_layout(
                height=350,
                paper_bgcolor="#0f172a",
                font={"color": "white"},
                margin=dict(l=20, r=20, t=40, b=20)
            )

            st.plotly_chart(
                gauge,
                use_container_width=True
            )
