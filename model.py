import matplotlib.pyplot as plt

population = 1000

S = 999
I = 1
R = 0

beta = 0.3
gamma = 0.1

susceptible = []
infected = []
recovered = []

for day in range(100):

    new_infections = beta * S * I / population
    new_recoveries = gamma * I

    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    susceptible.append(S)
    infected.append(I)
    recovered.append(R)

plt.plot(susceptible, label="Susceptible")
plt.plot(infected, label="Infected")
plt.plot(recovered, label="Recovered")

plt.xlabel("Days")
plt.ylabel("People")
plt.title("SIR Disease Spread Model")

plt.legend()
plt.show()