import streamlit as st
import matplotlib.pyplot as plt

st.title("Disease Spread Simulator")
disease = st.selectbox(
    "Disease",
    ["Custom", "Flu", "COVID-19", "Measles"]
)
if disease == "Flu":
    beta = 0.2
    gamma = 0.1

elif disease == "COVID-19":
    beta = 0.4
    gamma = 0.1

elif disease == "Measles":
    beta = 0.8
    gamma = 0.1

population = st.slider(
    "Population",
    100,
    10000,
    1000
)

beta = st.slider(
    "Infection Rate",
    0.0,
    1.0,
    0.3
)

gamma = st.slider(
    "Recovery Rate",
    0.0,
    1.0,
    0.1
)

days = st.slider(
    "Days",
    10,
    300,
    100
)

S = population - 1
I = 1
R = 0

susceptible = []
infected = []
recovered = []

for day in range(days):

    new_infections = beta * S * I / population
    new_recoveries = gamma * I

    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    susceptible.append(S)
    infected.append(I)
    recovered.append(R)
peak_infections = max(infected)

st.metric(
    "Peak Infections",
    f"{peak_infections:.0f}"
)

fig, ax = plt.subplots()

ax.plot(susceptible, label="Susceptible")
ax.plot(infected, label="Infected")
ax.plot(recovered, label="Recovered")

ax.legend()
ax.set_title("Disease Spread Simulation")
ax.set_xlabel("Days")
ax.set_ylabel("Population")

st.pyplot(fig)