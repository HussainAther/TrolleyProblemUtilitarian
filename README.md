# A Utilitarian Solution to the Trolley Problem

## Trolley Problem and Self-driving Cars

Self-driving cars may take us wherever we want to go, but they won’t know where unless we tell them. And with the first death of a man riding autopilot in a self-driving car, we find ourselves with the same old questions we’ve always had. What should an autonomous car do when human life is at stake?

The ethical dilemma of whether a car should swerve out of the way to kill one person in order to save others is a form of the trolley problem. Now, engineers, scientists, and policymakers ask the big questions philosophers have debated for centuries.

The question is driven by our ethical concerns for the general public. We make these decisions with regards to the effects they have on our society as a whole. Self-interest usually takes the backseat, and our idealistic utopias emerge. We’d love to live in a world in which a car can simply calculate the risks and benefits of various decisions to which action to take. And, in this sense, the decisions of self-driving cars aren’t too different from our current methods of engineering. When we make airbags, we design them so that they would save as many people as possible while taking into account the costs of manufacturing.

The experimental ethics approach of Jean-François Bonnefon, researcher at the Toulouse School of Economics, probes the big questions for answers. By surveying the public and designing experiments that take into account various situations of self-driving cars, we can get a general idea of how people view them. The researchers ask questions to the public about different scenarios and how they would want their cars to act. This includes the general situations of swerving out of the way of a crowd of people in order to hit one person, but also more variable specific cases, such picturing yourself in the self-driving car, as opposed to someone else. It would take those opinions of the public into account so that the designers of self-driving cars can program their cars with their thoughts in mind.

It seems reasonable and straightforward. Cars would perform the actions which result in the fewest deaths. But let’s not let the idealism of utilitarian motives get the best of us. The same study showed that, though people preferred cars to drive this way, they wouldn’t want to buy cars or be the drivers of them. No one wants to be the driver of the car that makes the decision to swerve and kill a single person in order to save the lives of a greater number of people. The findings illustrate the conclusion quite well. When people have an overall goal for the public in mind, that is, protecting the lives of as many people as possible, they agree it should be pursued. But every individual person doesn’t find it in their own self-interests to do it.

What this means is we need a greater social change in our understanding of ethics before we can put our own solutions into action. Some sort of a collective understanding of individual decisions being part of a bigger picture would lessen the burden on the single consumer in buying a self-driving car. The experimental ethics work should also encompass what the outcomes of those automatic driving decisions are.

## Ethics as maximizing happiness: Utilitarianism
In the famous Trolley problem philosopher Philippa Foot introduced in the 1960s, you have the ability to pull a lever to divert a train from running over five tied-up people lying on the tracks. If you pull the lever, the trolley will be redirected onto a side track, and the five people on the main track will be saved. However, there is a single person lying on the side track.

According to classical utilitarianism (the view that the morally right action is the action that produces the most good), pulling the lever would be permissible and more moral. English philosophers Jeremy Bentham and John Stuart Mill introduced utilitarianism as the sole moral obligation to maximize happiness. As an alternative to divine, religious theories of ethics. Utilitarianism suffers from the idea of “utility monsters,” individuals who would have much more happiness (and therefore utility) than average. This would cause actions to skew towards and exploit maximizing the monster’s happiness in such a way that others would suffer. Since philosopher Robert Nozick introduced the “utility monster” idea in 1974, it has been discussed in politics as driving the ideas of special interest groups and free speech – as though securing these interests would serve the interests of the few experiencing much more happiness than the general population.

## Solving the Trolley Problem using Utilitariansim
For this project, we can solve the Trolley problem using Python! We implement a basic, simplified utilitarian method of reasoning to solve the trolley problem. The problem consists of deciding whether to pull a lever that would change the track of an incoming train such that it would kill fewer people tied to the tracks. 

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

## References
Jean-François Bonnefon, Azim Shariff, & Iyad Rahwan (2015). The social dilemma of autonomous vehicles Science, 352(6293), 1573-1576 (2016) arXiv: 1510.03346v2

