In today's lesson we finish covering chapter 1 of the book, looking more at test/validation sets, avoiding machine learning project failures, and the foundations of transfer learning.

Then we move on to looking at the critical machine learning topic of evidence, including discussing confidence intervals, priors, and the use of visualization to better understand evidence.

Finally, we begin our look into productionization of models (chapter 2 of the book), including discussing the overall project plan for model development, and how to create your own datasets. Here's a helpful [forum post](https://forums.fast.ai/t/getting-the-bing-image-search-key/67417) explaining how to get the Bing API key you'll need for downloading images.

## Questionnaire

(If you're not sure of the answer to a question, try watching the next lesson and then coming back to this one, or read the first two chapters of the book.)

1. Can we always use a random sample for a validation set? Why or why not?
1. What is overfitting? Provide an example.
1. What is a metric? How does it differ from "loss"?
1. How can pretrained models help?
1. What is the "head" of a model?
1. What kinds of features do the early layers of a CNN find? How about the later layers?
1. Are image models only useful for photos?
1. What is an "architecture"?
1. What is segmentation?
1. What is `y_range` used for? When do we need it?
1. What are "hyperparameters"?
1. What's the best way to avoid failures when using AI in an organization?
1. What is a p value?
1. What is a prior?
1. Provide an example of where the bear classification model might work poorly in production, due to structural or style differences in the training data.
1. Where do text models currently have a major deficiency?
1. What are possible negative societal implications of text generation models?
1. In situations where a model might make mistakes, and those mistakes could be harmful, what is a good alternative to automating a process?
1. What kind of tabular data is deep learning particularly good at?
1. What's a key downside of directly using a deep learning model for recommendation systems?
1. What are the steps of the Drivetrain Approach?
1. How do the steps of the Drivetrain Approach map to a recommendation system?
1. Create an image recognition model using data you curate, and deploy it on the web.
1. What is `DataLoaders`?
1. What four things do we need to tell fastai to create `DataLoaders`?
1. What does the `splitter` parameter to `DataBlock` do?
1. How do we ensure a random split always gives the same validation set?
