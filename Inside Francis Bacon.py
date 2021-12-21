from nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt
#
#
#
# The New Atlantis
#
#
corpus_root = './data'
filelists = PlaintextCorpusReader(corpus_root, '.*')
filelists.fileids()
wordslist = filelists.words('The New Atlantis.txt')
#
# Frequency distribution
#
fdist = FreqDist(wordslist)
#
# Plot the frequency distribution of 40 words with
# cumulative = True
#
fdist.plot(40, cumulative=True, title='Total Word Frequency(The New Atlantis)')
#
# Print words having 7 or more characters which occured for 5 or more times
#
frequent_words = [[fdist[word], word] for word in set(wordslist) 
                  if len(word) > 6 and fdist[word] >= 5 
                  and word != 'another' and word != 'strange'
                  and word != 'brought' and word != 'persons' 
                  and word != 'somewhat' and word != 'whereof' 
                  and word != 'themselves' and word != 'amongst' 
                  and word != 'excellent' and word != 'several' 
                  and word != 'greater' and word != 'ourselves' 
                  and word != 'without' and word != 'likewise' 
                  and word != 'desired' and word != 'nothing'
                  and word != 'together' and word != 'whether'
                  and word != 'because' and word != 'blessing'
                  and word != 'company' and word != 'further'
                  and word != 'himself' and word != 'therefore'
                  and word != 'thought' and word != 'against'
                  and word != 'strangers' and word != 'towards'
                  and word != 'nations' and word != 'represent'
                  and word != 'answered' and word != 'variety'
                  and word != 'unknown' and word != 'fellows'
                  and word != 'besides' and word != 'between'
                  and word != 'certain' and word != 'colours'
                  and word != 'countries' and word != 'friends'
                  and word != 'otherwise' and word != 'receive'
                  and word != 'relation' and word != 'strength'
                  and word != 'through' and word != 'whereby'
                  and word != 'wherein' and word != 'strangers'
                  and word != 'Therefore' and word != 'appointed'
                  and word != 'especially' and word != 'greatest'
                  and word != 'hundred' and word != 'mountains'
                  and word != 'respect' and word != 'seemeth'
                  and word != 'sometimes' and word != 'thousand'
                  #and word != '' and word != ''
                  ]
#
# Record the frequency count of
#
sorted_word_frequencies = {}
for item in sorted(frequent_words):
    sorted_word_frequencies[item[1]] = item[0]
#
# Create the plot
#
plt.figure()
plt.bar(range(len(sorted_word_frequencies)), list(sorted_word_frequencies.values()), align='center')
plt.xticks(range(len(sorted_word_frequencies)), list(sorted_word_frequencies.keys()), rotation=80, fontsize=10)
plt.title("Frequent Words(The New Atlantis)", fontsize=18)
plt.xlabel("Words", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.show()
#
#
#
# The Advancement of Learning
#
#
corpus_root = './data'
filelists = PlaintextCorpusReader(corpus_root, '.*')
filelists.fileids()
wordslist = filelists.words('The Advancement of Learning.txt')
#
# Frequency distribution
#
fdist = FreqDist(wordslist)
#
# Plot the frequency distribution of 40 words with
# cumulative = True
#
fdist.plot(40, cumulative=True, title='Total Word Frequency(The Advancement of Learning)')
#
# Print words having 7 or more characters which occured for 30 or more times
#
frequent_words_2 = [[fdist[word], word] for word in set(wordslist) 
                  if len(word) > 6 and fdist[word] >= 30
                  and word != 'Neither' and word != 'general'
                  and word != 'although' and word != 'according' 
                  and word != 'conclude' and word != 'Another' 
                  and word != 'example' and word != 'nevertheless'
                  and word != 'whereas' and word != 'concerning'
                  and word != 'knowledge' and word != 'received'
                  and word != 'deficient' and word != 'handled'
                  and word != 'opinions' and word != 'inquiry'
                  and word != 'somewhat' and word != 'actions'
                  and word != 'present' and word != 'several'
                  and word != 'variety' and word != 'certain'
                  and word != 'sometimes' and word != 'against'
                  and word != 'between' and word != 'persons'
                  and word != 'another' and word != 'excellent'
                  and word != 'seemeth' and word != 'himself'
                  and word != 'particular' and word != 'thereof'
                  and word != 'touching' and word != 'likewise'
                  and word != 'without' and word != 'whereof'
                  and word != 'themselves' and word != 'because'
                  and word != 'therefore' and word != 'rather'
                  and word != 'wherein' and word != 'learned'
                  and word != 'towards' and word != 'further'
                  and word != 'nothing' and word != 'whether'
                  and word != 'natures' and word != 'princes'
                  #and word != '' and word != ''
                  ]
#
# Record the frequency count of
#
sorted_word_frequencies_2 = {}
for item in sorted(frequent_words_2):
    sorted_word_frequencies_2[item[1]] = item[0]
#
# Create the plot
#
plt.figure()
plt.bar(range(len(sorted_word_frequencies_2)), list(sorted_word_frequencies_2.values()), align='center')
plt.xticks(range(len(sorted_word_frequencies_2)), list(sorted_word_frequencies_2.keys()), rotation=80, fontsize=8)
plt.title("Frequent Words(The Advancement of Learning)", fontsize=18)
plt.xlabel("Words", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.show()
#
#
# 
# Bacon's Essays
# 
#
corpus_root = './data'
filelists = PlaintextCorpusReader(corpus_root, '.*')
filelists.fileids()
wordslist = filelists.words("Bacon's Essays.txt")
#
# Frequency distribution
#
fdist = FreqDist(wordslist)
#
# Plot the frequency distribution of 40 words with
# cumulative = True
#
fdist.plot(40, cumulative=True, title="Total Word Frequency(Bacon's Essays)")
#
# Print words having 7 or more characters which occured for 25 or more times
#
frequent_words_3 = [[fdist[word], word] for word in set(wordslist) 
                  if len(word) > 6 and fdist[word] >= 25
                  and word != 'opinion' and word != 'perhaps'
                  and word != 'matters' and word != 'princes'
                  and word != 'EXPLAINED' and word != 'Explained'
                  and word != 'certainly' and word != 'greater'
                  and word != 'amongst' and word != 'neither'
                  and word != 'together' and word != 'pleasure'
                  and word != 'published' and word != 'strength'
                  and word != 'greatness' and word != 'particular'
                  and word != 'whereof' and word != 'especially'
                  and word != 'somewhat' and word != 'received'
                  and word != 'knowledge' and word != 'themselves'
                  and word != 'greatest' and word != 'towards'
                  and word != 'thought' and word != 'commonly'
                  and word != 'sometimes' and word != 'certain'
                  and word != 'against' and word != 'another'
                  and word != 'persons' and word != 'because'
                  and word != 'therefore' and word != 'themselves'
                  and word != 'himself' and word != 'nothing'
                  and word != 'account' and word != 'Certainly'
                  and word != 'edition' and word != 'mankind'
                  and word != 'subject' and word != 'general'
                  and word != 'likewise' and word != 'enlarged'
                  and word != 'without' and word != 'between'
                  and word != 'through' and word != 'thereof'
                  and word != 'occasion' and word != 'generally'
                  and word != 'wherein' and word != 'EXPLANATION'
                  and word != 'whereby' and word != 'according'
                  and word != 'respect' and word != 'brought'
                  and word != 'authority' and word != 'further'
                  #and word != '' and word != ''
                  ]
#
# Record the frequency count of
#
sorted_word_frequencies_3 = {}
for item in sorted(frequent_words_3):
    sorted_word_frequencies_3[item[1]] = item[0]
#
# Create the plot
#
plt.figure()
plt.bar(range(len(sorted_word_frequencies_3)), list(sorted_word_frequencies_3.values()), align='center')
plt.xticks(range(len(sorted_word_frequencies_3)), list(sorted_word_frequencies_3.keys()), rotation=80, fontsize=8)
plt.title("Frequent Words(Bacon's Essays)", fontsize=18)
plt.xlabel("Words", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.show()
#
#
#
# All Together
#
corpus_root = './data'
filelists = PlaintextCorpusReader(corpus_root, '.*')
filelists.fileids()
wordslist = filelists.words('All Together.txt')
#
# Frequency distribution
#
fdist = FreqDist(wordslist)
#
# Plot the frequency distribution of 40 words with
# cumulative = True
#
fdist.plot(40, cumulative=True, title='Total Word Frequency(All Together)')
#
# Print words having 7 or more characters which occured for 50 or more times
#
frequent_words_4 = [[fdist[word], word] for word in set(wordslist) 
                  if len(word) > 6 and fdist[word] >= 50
                  and word != 'another' and word != 'strange'
                  and word != 'brought' and word != 'persons' 
                  and word != 'somewhat' and word != 'whereof' 
                  and word != 'themselves' and word != 'amongst' 
                  and word != 'excellent' and word != 'several' 
                  and word != 'greater' and word != 'ourselves' 
                  and word != 'without' and word != 'likewise' 
                  and word != 'desired' and word != 'nothing'
                  and word != 'together' and word != 'whether'
                  and word != 'because' and word != 'blessing'
                  and word != 'company' and word != 'further'
                  and word != 'himself' and word != 'therefore'
                  and word != 'thought' and word != 'against'
                  and word != 'strangers' and word != 'towards'
                  and word != 'nations' and word != 'represent'
                  and word != 'answered' and word != 'variety'
                  and word != 'unknown' and word != 'fellows'
                  and word != 'besides' and word != 'between'
                  and word != 'certain' and word != 'colours'
                  and word != 'countries' and word != 'friends'
                  and word != 'otherwise' and word != 'receive'
                  and word != 'relation' and word != 'strength'
                  and word != 'through' and word != 'whereby'
                  and word != 'wherein' and word != 'strangers'
                  and word != 'Therefore' and word != 'appointed'
                  and word != 'especially' and word != 'greatest'
                  and word != 'hundred' and word != 'mountains'
                  and word != 'respect' and word != 'seemeth'
                  and word != 'sometimes' and word != 'thousand'
                  and word != 'Neither' and word != 'general'
                  and word != 'although' and word != 'according' 
                  and word != 'conclude' and word != 'Another' 
                  and word != 'example' and word != 'nevertheless'
                  and word != 'whereas' and word != 'concerning'
                  and word != 'knowledge' and word != 'received'
                  and word != 'deficient' and word != 'handled'
                  and word != 'opinions' and word != 'inquiry'
                  and word != 'somewhat' and word != 'actions'
                  and word != 'present' and word != 'several'
                  and word != 'variety' and word != 'certain'
                  and word != 'sometimes' and word != 'against'
                  and word != 'between' and word != 'persons'
                  and word != 'another' and word != 'excellent'
                  and word != 'seemeth' and word != 'himself'
                  and word != 'particular' and word != 'thereof'
                  and word != 'touching' and word != 'likewise'
                  and word != 'without' and word != 'whereof'
                  and word != 'themselves' and word != 'because'
                  and word != 'therefore' and word != 'rather'
                  and word != 'opinion' and word != 'perhaps'
                  and word != 'matters' and word != 'princes'
                  and word != 'EXPLAINED' and word != 'Explained'
                  and word != 'certainly' and word != 'greater'
                  and word != 'amongst' and word != 'neither'
                  and word != 'together' and word != 'pleasure'
                  and word != 'published' and word != 'strength'
                  and word != 'greatness' and word != 'particular'
                  and word != 'whereof' and word != 'especially'
                  and word != 'somewhat' and word != 'received'
                  and word != 'knowledge' and word != 'themselves'
                  and word != 'greatest' and word != 'towards'
                  and word != 'thought' and word != 'commonly'
                  and word != 'sometimes' and word != 'certain'
                  and word != 'against' and word != 'another'
                  and word != 'persons' and word != 'because'
                  and word != 'therefore' and word != 'themselves'
                  and word != 'himself' and word != 'nothing'
                  and word != 'account' and word != 'Certainly'
                  and word != 'edition' and word != 'mankind'
                  and word != 'subject' and word != 'general'
                  and word != 'likewise' and word != 'enlarged'
                  and word != 'without' and word != 'between'
                  #and word != '' and word != ''
                  ]
#
# Record the frequency count of
#
sorted_word_frequencies_4 = {}
for item in sorted(frequent_words_4):
    sorted_word_frequencies_4[item[1]] = item[0]
#
# Create the plot
#
plt.figure()
plt.bar(range(len(sorted_word_frequencies_4)), list(sorted_word_frequencies_4.values()), align='center')
plt.xticks(range(len(sorted_word_frequencies_4)), list(sorted_word_frequencies_4.keys()), rotation=80, fontsize=10)
plt.title("Frequent Words(All Together)", fontsize=18)
plt.xlabel("Words", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.show()


    
    
