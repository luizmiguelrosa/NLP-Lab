# Word Repetition Classifier

Following a tip from an expert in the field, I decided to start a study of classification by word repetition. I tried to do something closer to what I had already seen with my text classifier, but I will refine the concepts used over time.

## Generation of Terms
First, a dictionary is generated with the repetition of each word related to an entity. For example: "hours" repeated 5 times in the entity "clock".
These repetitions are taken from texts attributed to entities, from these repetitions a probability can be calculated.

## Text Processing
In order for the functions to be able to manipulate and analyze the texts, they are processed, leaving them all in lower case and separating each word in a list.

## Predict Entity
First an input text is inserted into the function, which calculates a probability of having happened in each entity.