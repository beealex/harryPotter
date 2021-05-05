from collections import Counter
import pygal
import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.mode)  # 'rule'

filchFiggSpeech = open('filch_figgSpeeches.txt', 'r')
words = filchFiggSpeech.read()
wordstrings = str(words)
# print(wordstrings)

potterWords = nlp(wordstrings)
for token in potterWords:
     # if not token.is_punct:
    print(token.text, "---->", token.pos_, " ", spacy.explain(token.pos_), ":::::", token.lemma_)

def adjcollector(words):
    Adj = []
    count = 0
    for token in words:
        if token.pos_ == "ADJ":
            count += 1
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            # don't forget the underscore after token.lemma_ , token.pos_, etc.!
            Adj.append(token.lemma_)
            # print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    # print(count, ": ", Verbs)
    return Adj

listAdj = adjcollector(potterWords)
adj_freq = Counter(listAdj)
topTwenty = adj_freq.most_common(20)
print(topTwenty)
lastTen = adj_freq.most_common()[:-5:-1]
print(lastTen)

# bar_chartOver10 = pygal.Bar()
bar_chartTopTwenty = pygal.Bar()

# bar_chartOver10.title = 'Noun Lemma Forms in Disney Songs'
bar_chartTopTwenty.title= 'All Adjective Lemmas in Argus Filch and Arabella Figg Speeches'

# for a in adj_freq:
#     # verb_freq is a dictionary structure, so we return its key and its value:
#     print(a, adj_freq[a])
#     if adj_freq[a] > 10:
#         bar_chartOver10.add(a, adj_freq[a])


for t in topTwenty:
    # this is a list of tuples, so we return its values like this:
    print(t[0], t[1])
    bar_chartTopTwenty.add(t[0], t[1])

# print(bar_chart)
print(bar_chartTopTwenty.render(is_unicode=True))
# bar_chartOver10.render_to_file('bar_chartOver10.svg')
bar_chartTopTwenty.render_to_file('filchFigg_chartTopTwenty.svg')
