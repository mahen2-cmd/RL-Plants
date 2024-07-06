import mesa
import seaborn as sns
import numpy as np
import random
import pandas as pd


class MoneyAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        self.wealth = 1

    def step(self):
        # print(f"Hi I am an agent. You can call me {str(self.unique_id)}. And my wealth is {str(self.wealth)}")

        if self.wealth > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent is not None:
                other_agent.wealth += 1
                self.wealth -= 1


class MoneyModel(mesa.Model):
    def __init__(self, N):
        super().__init__()
        self.num_agents = N

        self.schedule = mesa.time.RandomActivation(self)

        for i in range(self.num_agents):
            a = MoneyAgent(i, self)

            self.schedule.add(a)

    def step(self):
        self.schedule.step()


model = MoneyModel(10)

for i in range(10):
    print()
    model.step()


agent_wealth = [a.wealth for a in model.schedule.agents]
g = sns.histplot(agent_wealth, discrete=True)
g.set(title="Wealth Distribution", xlabel="Wealth", ylabel="Number of Agents")





all_wealth = []

for j in range(100):
    model = MoneyModel(10)
    for i in range(10):
        model.step()

    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)


g = sns.histplot(all_wealth, discrete=True)
g.set(title="Wealth Distribution", xlabel="Wealth", ylabel="Number of agents")
