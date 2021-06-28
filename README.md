# Recommendation system for Netflix Movies and TV Shows
## Description
The challenge is to create a recommend systen that would offer the user relevant movies and/or tv shows based on the user's selected  movie
## Task
**Input data**: Netflix movie and tv show dataset, user selected movie
Netflix dataset contains the following features:
* Type: movie or tv show
* Title
* Director
* Cast
* Country
* Release year
* Rating
* Duration
* Genre list
* Date added
* Description

**Output data**: 5 relevant movies or/and tv shows
## Solution line
### Common information
Because of the origin dataset hasn't any users action information, the main course of solution will be a creation content based recommendation system  
In this case, 2 main approaches to the evaluation of relevance level were chosen:
* Based on general movies fearures similarity
* Based on analysis of description and title with nlp

Obtained assessments should be used together to form the final relevant movies list
### Methodology
There are different ways and approaches to solve the first challenge: to evaluate the similatiry between user movie and other available movies. But with no information about user action and desicion all of them will be just a theoretical way to approximate real user selection. So it would be one of the best way to realize the closest content based models and make a evaluative decision which models are the most successful for the challenge. And, of course, the real correctness and accordance of each methods must be defined in the practical tests. Moreover, the knowledge of real user actions is the best and maybe the only one way to define the real weight of parameters of movies on similarity and relevance and increase accuracy of models. Also that information is the key to go to collaborative and hybrid relevant system

What about the second way, analysis of description and title, there should be used general nlp methods to find similatiry between objects, and, by analogy with the previous part, should be adapted for tests in production and weight updates

With a high probability the greatest effect will be obtained with not only one methods of calculation but in interaction of different ways and approaches. First of all it's applied to main approaches when calculation of movie information similarity and results of description analysis will be mixing to receive the most comprehensive assessment. But the probability that some methods inside both approaches would complement each other is by no means excluded

Some methods and approaches that should be realized and tested during work with general movie features and similarity calculation:
* Similarity measures
* Various cluster algorithms and methods
* Kernel machines
* Regressional analysis
* Classificational methods, etc

Also general approaches of nlp - statiscitcal and neural nlp methods - should be used for the alalysis of description and title to define similarity measure between objects 
