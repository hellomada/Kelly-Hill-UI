import streamlit as st
import requests
import time

# Your Make.com webhook (replace with your own if needed)
WEBHOOK_URL = "https://hook.us2.make.com/j5av448r5zrnlib5ao4df3becae8y45t"

st.set_page_config(page_title="Make.com Trigger", page_icon="⚡", layout="centered")

st.title("⚡ Run Make.com Automation")
st.write("Click below to trigger the Make.com scenario.")

# User input for number of runs
num_runs = st.number_input("How many times do you want to run it?", min_value=1, max_value=20, value=1, step=1)

# Button to trigger Make automation
if st.button("▶ Run for Kelly"):
    st.write(f"Running scenario {num_runs} time(s)...")

    responses = []
    for i in range(num_runs):
        try:
            # Send POST request to webhook
            r = requests.post(WEBHOOK_URL, json={"user": "Kelly", "run_number": i+1})
            
            if r.status_code == 200:
                responses.append(r.json() if r.headers.get("Content-Type") == "application/json" else r.text)
                st.success(f"Run {i+1}: Success ✅")
            else:
                responses.append(f"Error {r.status_code}: {r.text}")
                st.error(f"Run {i+1}: Failed ❌")
            
            # Optional delay between runs
            time.sleep(1)

        except Exception as e:
            st.error(f"Run {i+1}: Exception - {e}")
            responses.append(str(e))

    st.subheader("Returned Data from Webhook:")
    for i, res in enumerate(responses, start=1):
        st.write(f"Run {i} result:", res)
