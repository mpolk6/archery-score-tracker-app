import streamlit as st

st.title("Archery Score & Tracking App")

name = st.text_input("Archer Name")
bow_type = st.selectbox("Bow Type", ["Olympic Recurve", "Barebow Recurve", "Compound"])
distance = st.selectbox("Distance", ["10m", "20m", "30m", "50m", "70m"])

scores = []
for i in range(1, 7):
    scores.append(st.number_input(f"End {i} Score", min_value=0, max_value=30, step=1))

if st.button("Calculate Score"):
    total = sum(scores)
    average = total / 6

    if average < 10:
        level = "Beginner"
        message = "Keep practicing!"
    elif average <= 20:
        level = "Intermediate"
        message = "Nice job!"
    elif average <= 29:
        level = "Advanced"
        message = "Awesome shooting!"
    else:
        level = "Master"
        message = "Perfect Score!"

    if average < 15:
        team = "Beginner Team"
    elif average <= 22:
        team = "Intermediate Team"
    else:
        team = "Advanced Team"

    st.subheader("Results")
    st.write("Name:", name)
    st.write("Bow Type:", bow_type)
    st.write("Distance:", distance)
    st.write("Total Score:", total)
    st.write("Average Score:", round(average, 2))
    st.write("Skill Level:", level)
    st.write("Suggested Team Placement:", team)
    st.write(message)