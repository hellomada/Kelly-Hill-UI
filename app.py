import streamlit as st
import requests
import time

# ✅ Updated Make.com webhook
WEBHOOK_URL = "https://hook.us2.make.com/53ukil5o92wgrmencm8a18p414csz34x"

st.set_page_config(page_title="Make.com Trigger", page_icon="⚡", layout="centered")

st.title("⚡ Run Make.com Automation")
st.write("Click below to trigger the Make.com scenario.")

# User input for number of runs
num_runs = st.number_input(
    "How many times do you want to run it?",
    min_value=1, max_value=20, value=1, step=1
)

# ✅ Add toggle for newsletter/blog extras
extras_requested = st.checkbox("Include newsletter & blog extras?", value=False)

# Button to trigger Make automation
if st.button("▶ Run for Kelly"):
    st.write(f"Running scenario {num_runs} time(s)...")

    responses = []
    for i in range(num_runs):
        try:
            # Send POST request to webhook with extras_requested
            payload = {
                "user": "Kelly",
                "run_number": i + 1,
                "extras_requested": extras_requested
            }
            
            r = requests.post(WEBHOOK_URL, json=payload)
            
            if r.status_code == 200:
                try:
                    res = r.json()
                except ValueError:
                    res = r.text

                responses.append(res)
                st.success(f"Run {i+1}: Success ✅")
            else:
                res = f"Error {r.status_code}: {r.text}"
                responses.append(res)
                st.error(f"Run {i+1}: Failed ❌")
            
            time.sleep(1)  # optional delay

        except Exception as e:
            res = f"Exception: {e}"
            responses.append(res)
            st.error(f"Run {i+1}: Exception - {e}")

    st.subheader("📩 Returned Data from Webhook:")
    for i, res in enumerate(responses, start=1):
        st.json(res) if isinstance(res, dict) else st.write(f"Run {i} result:", res)
