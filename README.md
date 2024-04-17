# LINX
This repository contains the source code and experiments used to evaluate LINX, a framework for autogenerating goal-oriented exploration notebook using a Natural Language Interface. 
The repository is free for use for academic purposes. Please contact the repository owners before usage.

## The Goal-oriented ADE problem: Generate an exploration session given a user's dataset and analysis goal
One of the most effective methods for facilitating the process of exploring a dataset is to examine pre-existing data exploration notebooks that contain curated exploration sessions that demonstrate interesting hypotheses and conjectures on the data. 
While numerous Automated Data Exploration (ADE) systems have been devised in previous work, they focus on assiting users explore a *new* dataset, showing generally interesting patterns that are ineffective for goal-oriented exploration where the users need to answer specific questions about the data. 

LIN is a generative system augmented with a natural language interface for goal-oriented ADE.
It takes as input a dataset an analysis goal in natural language, then generates a personalized exploration session that is relevant to the user's goal.

LINX has two main compoenets: (1) An LLM-based solution the interprets the analysis goal and derive a set of specification for the output exploration session, (2)  A modular ADE engine based on Constrained Deep Reinforcement Learning (CDRL), which consider the specifications in its optimization process, thus yielding high-utility sessions that are relevant to the analysis goal. 




## [Source Code](src)
The source code is located [here](src) (LINX/src) <br/>
Under this directory, there are two folders:
1. LLM-Based Solution for Deriving Specifications: contains all the source code of the LLM component for deriving exploration specifications given a user's goal and dataset.
2. CDRL ADE Engine: contains all the source code of the CDRL engine that generating the personalized exploration notebooks.
For installation guide, running instructions and further details please refer to the 
documentation under the source code directory in the link above.

## [Documentation](documentation)
1. [LINX Technical Report ](documentation/LINX_Full_Paper.pdf) - Including a comprehensive appendix with complete details is a vailable  [here](documentation/LINX_Full_Paper.pdf).
2. [LDX Language Guide](documentation/LDX_User_Guide.pdf)
    Full Details and Examples for our specification language for data exploration are available [here](documentation/LDX_User_Guide.pdf). <br/>

## [Experiment Datasets](datasets)
The datasets used in our empirical evaluation are located [here](datasets). <br/>
LINX is tested on 3 different datasets:
1. Netflix Movies and TV-Shows: list of Netflix titles, each title is described using 11 features such as the country of production, duration/num. of seasons, etc.
2. Flight-delays: Each record describes a domestic US flight, using 12 attributes such as origin/destination airport, flight duration, issuing airline, departure delay times, delay reasons, etc.
3. Google Play Store Apps: A collection of mobile apps available on the Google Play Store. Each app is described using 11 features, such as name, category, price, num. of installs, reviews, etc.

## [Goal-oriented ADE Benchamrk](nl2ldx_benchmark)
We provide a new benchmark dataset for the task of goal-oriented ADE, available [here](<nl2ldx_benchmark/NL2LDX-benchmark.json>).  <br/>
The benchmark contains 182 instances of analytical goals and ocrresponding exploration specifications. 
This folder includes also a dedicated notebook for evaluating models on this benchmark, located [here](<nl2ldx_benchmark/evaulation/evaluation_notebook.ipynb>), 
and as well the evaluation results of our models.

## [Additional Experiments](additional_experiments)
This folder contains information about:
1. [User Study](additional_experiments/user_study) - The exploration notebooks generated by either LINX and the baselines are located [here](additional_experiments/user_study). <br/>
In the given link you can find the exploratory sessions that were presented to each participant of the user study.
The directory structure is as: `<Dataset>/<Task>/<Baseline>.ipynb` (the identity of the baseline was not disclosed to the participants).
For the ChatGPT-based notebooks, we also provide the prompt and raw output. 
2. [Convergence Test](additional_experiments/convergence) - The convergence and running times of our CDRL engine located [here](additional_experiments/convergence).


