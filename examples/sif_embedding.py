import sys
sys.path.append('../src')
import data_io, params, SIF_embedding

# input
wordfile = '../data/glove.840B.300d.txt' # word vector file, can be downloaded from GloVe website
weightfile = '../auxiliary_data/enwiki_vocab_min200.txt' # each line is a word and its frequency
weightpara = 1e-3 # the parameter in the SIF weighting scheme, usually in the range [3e-5, 3e-3]
rmpc = 1 # number of principal components to remove in SIF weighting scheme

sentences = ['this is an example sentence', 'this is another sentence that is slightly longer', 'the food was good not bad at all', 'the food was bad not good at all']
# load word vectors
(words, We) = data_io.getWordmap(wordfile)
print ("Reading GloVe words:vectors ... Complete")
# load word weights
word2weight = data_io.getWordWeight(weightfile, weightpara) # word2weight['str'] is the weight for the word 'str'
print ("Computing weights from count file ... Complete")
weight4ind = data_io.getWeight(words, word2weight) # weight4ind[i] is the weight for the i-th word
print ("Setting the weights to corresponding GloVe words ... Complete")

# load sentences
result = data_io.sentences2idx(sentences, words) # x is the array of word indices, m is the binary mask indicating whether there is a word in that location

if len(result) > 1:
    x = result[0]
    m = result[1]

w = data_io.seq2weight(x, m, weight4ind) # get word weights

# set parameters
params = params.params()
params.rmpc = rmpc
# get SIF embedding
embedding = SIF_embedding.SIF_embedding(We, x, w, params) # embedding[i,:] is the embedding for sentence i

print (embedding[0, :])
print (embedding[1, :])
print (embedding[2, :])
print (embedding[3, :])
