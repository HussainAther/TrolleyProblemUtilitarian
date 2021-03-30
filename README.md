# A Utilitarian Solution to the Trolley Problem

## Ethics as maximizing happiness: Utilitarianism
In the famous Trolley problem philosopher Philippa Foot introduced in the 1960s, you have the ability to pull a lever to divert a train from running over five tied-up people lying on the tracks. If you pull the lever, the trolley will be redirected onto a side track, and the five people on the main track will be saved. However, there is a single person lying on the side track.

According to classical utilitarianism (the view that the morally right action is the action that produces the most good), pulling the lever would be permissible and more moral. English philosophers Jeremy Bentham and John Stuart Mill introduced utilitarianism as the sole moral obligation to maximize happiness. As an alternative to divine, religious theories of ethics. Utilitarianism suffers from the idea of “utility monsters,” individuals who would have much more happiness (and therefore utility) than average. This would cause actions to skew towards and exploit maximizing the monster’s happiness in such a way that others would suffer. Since philosopher Robert Nozick introduced the “utility monster” idea in 1974, it has been discussed in politics as driving the ideas of special interest groups and free speech – as though securing these interests would serve the interests of the few experiencing much more happiness than the general population.

## Solving the Trolley Problem using Utilitariansim
For this project, we can solve the Trolley problem using Python!

We implement a basic, simplified utilitarian method of reasoning to solve the trolley problem. The problem consists of deciding whether to pull a lever that would change the track of an incoming train such that it would kill fewer people tied to the tracks. 

Given a directed graph as an input file and a nonnegative integer attached to each edge (the number of people tied to that track). Still, this argument has its limits. It assumes each human has the same utility and that changing the path the train would take is completely within our control. It also doesn't  address the question of what caused the scenario to begin with (e.g., how did you find yourself in a case in which you have to resort to pullling a lever to save the lives of others?)

```
def trolley(y):
    """
    Given input graph of the trolley problem, calculate the optimal route that kills the 
    fewest number of people. The input y is a list of dictionaries to describe the neighbors 
    and number of people trapped to each track. The dictionary should use each key as the node 
    and entries as the neighbors and number of people on the track connecting that node to neighbor.
    """
    s = 0
    p = []
    f = 0
    mini = min(y(d, s+d[f][t], p+[f],t) for t in d[f]) 
    return f in p and s or mini
  ```
