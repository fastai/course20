We finish this course with a full lesson on natural language processing (NLP). Modern NLP depends heavily on *self-supervised learning*, and in particular the use of *language models*.

Pretrained language models are fine-tuned, in order to benefit from transfer learning. Unlike computer vision, fine-tuning in NLP can take advantage of an extra step, which is the use of self-supervised learning on the target dataset.

Before we can do any modeling with text data, we first have to tokenize and numericalize it. There are a number of approaches to tokenization, and which you choose will depend on your language and dataset.

NLP models use the same basic approach of *entity embedding* that we've seen before, except that for text data it's called `word embedding`. The method, however, is nearly identical.

NLP models have to handle documents of varying sizes, so they require a somewhat different architecture, such as a *recurrent neural network* (RNN). It turns out that an RNN is basically just a regular deep net, which has been refactored using a loop.

However, simple RNNs suffer from exploding gradients, so we have to use methods such as the LSTM cell to avoid this problem.

Finally, we look at some tricks to improve the results of our NLP models, such as additional regularization approaches, including various types of *dropout*, and activation regularization, as well as looking at weight tying.

## Questionnaire

1. What is "self-supervised learning"?
1. What is a "language model"?
1. Why is a language model considered self-supervised?
1. What are self-supervised models usually used for?
1. Why do we fine-tune language models?
1. What are the three steps to create a state-of-the-art text classifier?
1. How do the 50,000 unlabeled movie reviews help us create a better text classifier for the IMDb dataset?
1. What are the three steps to prepare your data for a language model?
1. What is "tokenization"? Why do we need it?
1. Name three different approaches to tokenization.
1. What is `xxbos`?
1. List four rules that fastai applies to text during tokenization.
1. Why are repeated characters replaced with a token showing the number of repetitions and the character that's repeated?
1. What is "numericalization"?
1. Why might there be words that are replaced with the "unknown word" token?
1. With a batch size of 64, the first row of the tensor representing the first batch contains the first 64 tokens for the dataset. What does the second row of that tensor contain? What does the first row of the second batch contain? (Careful—students often get this one wrong! Be sure to check your answer on the book's website.)
1. Why do we need padding for text classification? Why don't we need it for language modeling?
1. What does an embedding matrix for NLP contain? What is its shape?
1. What is "perplexity"?
1. Why do we have to pass the vocabulary of the language model to the classifier data block?
1. What is "gradual unfreezing"?
1. Why is text generation always likely to be ahead of automatic identification of machine-generated texts?
1. If the dataset for your project is so big and complicated that working with it takes a significant amount of time, what should you do?
1. Why do we concatenate the documents in our dataset before creating a language model?
1. To use a standard fully connected network to predict the fourth word given the previous three words, what two tweaks do we need to make to ou model?
1. How can we share a weight matrix across multiple layers in PyTorch?
1. Write a module that predicts the third word given the previous two words of a sentence, without peeking.
1. What is a recurrent neural network?
1. What is "hidden state"?
1. What is the equivalent of hidden state in ` LMModel1`?
1. To maintain the state in an RNN, why is it important to pass the text to the model in order?
1. What is an "unrolled" representation of an RNN?
1. Why can maintaining the hidden state in an RNN lead to memory and performance problems? How do we fix this problem?
1. What is "BPTT"?
1. Write code to print out the first few batches of the validation set, including converting the token IDs back into English strings, as we showed for batches of IMDb data in <<chapter_nlp>>.
1. What does the `ModelResetter` callback do? Why do we need it?
1. What are the downsides of predicting just one output word for each three input words?
1. Why do we need a custom loss function for `LMModel4`?
1. Why is the training of `LMModel4` unstable?
1. In the unrolled representation, we can see that a recurrent neural network actually has many layers. So why do we need to stack RNNs to get better results?
1. Draw a representation of a stacked (multilayer) RNN.
1. Why should we get better results in an RNN if we call `detach` less often? Why might this not happen in practice with a simple RNN?
1. Why can a deep network result in very large or very small activations? Why does this matter?
1. In a computer's floating-point representation of numbers, which numbers are the most precise?
1. Why do vanishing gradients prevent training?
1. Why does it help to have two hidden states in the LSTM architecture? What is the purpose of each one?
1. What are these two states called in an LSTM?
1. What is tanh, and how is it related to sigmoid?
1. What is the purpose of this code in `LSTMCell`: `h = torch.stack([h, input], dim=1)`
1. What does `chunk` do in PyTorch?
1. Study the refactored version of `LSTMCell` carefully to ensure you understand how and why it does the same thing as the non-refactored version.
1. Why can we use a higher learning rate for `LMModel6`?
1. What are the three regularization techniques used in an AWD-LSTM model?
1. What is "dropout"?
1. Why do we scale the weights with dropout? Is this applied during training, inference, or both?
1. What is the purpose of this line from `Dropout`: `if not self.training: return x`
1. Experiment with `bernoulli_` to understand how it works.
1. How do you set your model in training mode in PyTorch? In evaluation mode?
1. Write the equation for activation regularization (in math or code, as you prefer). How is it different from weight decay?
1. Write the equation for temporal activation regularization (in math or code, as you prefer). Why wouldn't we use this for computer vision problems?
1. What is "weight tying" in a language model?