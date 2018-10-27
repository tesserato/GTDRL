---
title: "RL Abstract"
output: html_document
bibliography: bibliography.bib
---

# Abstract

Research in the interface of game theory and artificial intelligence, in the context of reinforcement learning [@sandholm1996multiagent] and neural networks [@horie1998neural] for instance, is being conducted since at last late nineties, and has lead to the discovery of some relevant results: @hu1998multiagent, for instance, proves that under certain conditions a Q-learning [@watkins1989learning] based multiagent framework converges to a Nash equilibrium (provided only one exists).

Further work by @hu2003nash proposed a refinement to the Q-learning algorithm, dubbed a Nash Q-learning, to improve convergence in noncooperative multiagent games, while @wang2003reinforcement formulated an algorithm that provably converges, in case of multiple Nash equilibria, to the optimal one.

In fact, research comparing reinforcement learning and game theoretic results continue to be developed until the present day.

With a somewhat different approach, @erev1998predicting proposed an analogous investigation focused on the development of predictive/descriptive general theories of behavior in settings where players did not possess perfect rationality, that outperform equilibrium predictions in real-world scenarios.

Of the recent developments in this direction, focused on elaboration of best real-world policies, perhaps the most noteworthy is the work of @mnih2015human, published in Nature, where agents learn human level policies in Atari games, introducing deep Q-learning in the scene; that line of research was further extended in @silver2016mastering, where an agent was trained to play the game Go, regarded as the most difficult classical game, to the level of besting the human European Go champion.

this paper provides a model for the formulation of game theory inspired policies for groups of agents able to move in a discrete grid and willing to fulfill diverging goals. The proposed model, designed to be as generic as possible, can further be tailored to a number of specific situations and can be regarded as a generalization of Stackelberg Security Games (in the sense that multiple individual agents are considered in each of the groups and mixed strategies are allowed for both groups), already modelled from Game Theoretic principles implemented via A.I. practices: "Security games is a novel area of research that is based on computational and behavioral game theory, while also incorporating elements of AI planning under uncertainty and machine learning." [@Tambe2015Stackelberg]

<!-- emergence of cooperation is mandatory; look also for strategic positioning of team members if no opponent is present, maybe some 'altruistic', self-sacrificing strategy emerges -->

<!-- • Description of the final model -->

The model, pre-trained with the assumption of rationality and perfect information, can effortlessly be adjusted on-line in the course of its real-world utilization, so as to improve its policy accounting for potential bounds in rationality and incomplete information.


Examples of real-world applications include border monitoring, fireman allocation, inspection schedule planning, smuggling suppression policies, among many others



keywords: Stackelberg Security Games, Game Theory, Machine Learning, Reinforcement Learning

# Bibliography