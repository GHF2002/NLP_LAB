'''Name:Asmita Hon 
Batch:B4
Roll no:71
Pract no 3: Generating the n-gram model using nltk'''
from nltk import ngrams

from nltk.util import ngrams
#unigram model
n = 1
sentence = 'Natural language processing studies interactions between humans and computers to find ways for computers to process written and spoken words similar to how humans do. The field blends computer science, linguistics and machine learning.Natural language processing studies interactions between humans and computers to find ways for computers to process written and spoken words similar to how humans do. The field blends computer science, linguistics and machine learning.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'Natural language processing studies interactions between humans and computers to find ways for computers to process written and spoken words similar to how humans do. The field blends computer science, linguistics and machine learning.Natural language processing studies interactions between humans and computers to find ways for computers to process written and spoken words similar to how humans do. The field blends computer science, linguistics and machine learning.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
#trigram model
n = 3
sentence = 'Natural language processing studies interactions between humans and computers to find ways for computers to process written and spoken words similar to how humans do. The field blends computer science, linguistics and machine learning.Natural language processing studies interactions between humans and computers to find ways for computers to process written and spoken words similar to how humans do. The field blends computer science, linguistics and machine learning.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)

#using text file input
from nltk import ngrams
file = open("/home/exam/NLP_LAB/ass04.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()


'''('Natural',)
('language',)
('processing',)
('studies',)
('interactions',)
('between',)
('humans',)
('and',)
('computers',)
('to',)
('find',)
('ways',)
('for',)
('computers',)
('to',)
('process',)
('written',)
('and',)
('spoken',)
('words',)
('similar',)
('to',)
('how',)
('humans',)
('do.',)
('The',)
('field',)
('blends',)
('computer',)
('science,',)
('linguistics',)
('and',)
('machine',)
('learning.Natural',)
('language',)
('processing',)
('studies',)
('interactions',)
('between',)
('humans',)
('and',)
('computers',)
('to',)
('find',)
('ways',)
('for',)
('computers',)
('to',)
('process',)
('written',)
('and',)
('spoken',)
('words',)
('similar',)
('to',)
('how',)
('humans',)
('do.',)
('The',)
('field',)
('blends',)
('computer',)
('science,',)
('linguistics',)
('and',)
('machine',)
('learning.',)
('Natural', 'language')
('language', 'processing')
('processing', 'studies')
('studies', 'interactions')
('interactions', 'between')
('between', 'humans')
('humans', 'and')
('and', 'computers')
('computers', 'to')
('to', 'find')
('find', 'ways')
('ways', 'for')
('for', 'computers')
('computers', 'to')
('to', 'process')
('process', 'written')
('written', 'and')
('and', 'spoken')
('spoken', 'words')
('words', 'similar')
('similar', 'to')
('to', 'how')
('how', 'humans')
('humans', 'do.')
('do.', 'The')
('The', 'field')
('field', 'blends')
('blends', 'computer')
('computer', 'science,')
('science,', 'linguistics')
('linguistics', 'and')
('and', 'machine')
('machine', 'learning.Natural')
('learning.Natural', 'language')
('language', 'processing')
('processing', 'studies')
('studies', 'interactions')
('interactions', 'between')
('between', 'humans')
('humans', 'and')
('and', 'computers')
('computers', 'to')
('to', 'find')
('find', 'ways')
('ways', 'for')
('for', 'computers')
('computers', 'to')
('to', 'process')
('process', 'written')
('written', 'and')
('and', 'spoken')
('spoken', 'words')
('words', 'similar')
('similar', 'to')
('to', 'how')
('how', 'humans')
('humans', 'do.')
('do.', 'The')
('The', 'field')
('field', 'blends')
('blends', 'computer')
('computer', 'science,')
('science,', 'linguistics')
('linguistics', 'and')
('and', 'machine')
('machine', 'learning.')
('Natural', 'language', 'processing')
('language', 'processing', 'studies')
('processing', 'studies', 'interactions')
('studies', 'interactions', 'between')
('interactions', 'between', 'humans')
('between', 'humans', 'and')
('humans', 'and', 'computers')
('and', 'computers', 'to')
('computers', 'to', 'find')
('to', 'find', 'ways')
('find', 'ways', 'for')
('ways', 'for', 'computers')
('for', 'computers', 'to')
('computers', 'to', 'process')
('to', 'process', 'written')
('process', 'written', 'and')
('written', 'and', 'spoken')
('and', 'spoken', 'words')
('spoken', 'words', 'similar')
('words', 'similar', 'to')
('similar', 'to', 'how')
('to', 'how', 'humans')
('how', 'humans', 'do.')
('humans', 'do.', 'The')
('do.', 'The', 'field')
('The', 'field', 'blends')
('field', 'blends', 'computer')
('blends', 'computer', 'science,')
('computer', 'science,', 'linguistics')
('science,', 'linguistics', 'and')
('linguistics', 'and', 'machine')
('and', 'machine', 'learning.Natural')
('machine', 'learning.Natural', 'language')
('learning.Natural', 'language', 'processing')
('language', 'processing', 'studies')
('processing', 'studies', 'interactions')
('studies', 'interactions', 'between')
('interactions', 'between', 'humans')
('between', 'humans', 'and')
('humans', 'and', 'computers')
('and', 'computers', 'to')
('computers', 'to', 'find')
('to', 'find', 'ways')
('find', 'ways', 'for')
('ways', 'for', 'computers')
('for', 'computers', 'to')
('computers', 'to', 'process')
('to', 'process', 'written')
('process', 'written', 'and')
('written', 'and', 'spoken')
('and', 'spoken', 'words')
('spoken', 'words', 'similar')
('words', 'similar', 'to')
('similar', 'to', 'how')
('to', 'how', 'humans')
('how', 'humans', 'do.')
('humans', 'do.', 'The')
('do.', 'The', 'field')
('The', 'field', 'blends')
('field', 'blends', 'computer')
('blends', 'computer', 'science,')
('computer', 'science,', 'linguistics')
('science,', 'linguistics', 'and')
('linguistics', 'and', 'machine')
('and', 'machine', 'learning.')
For sentence 1 , trigrams are: 
('The', 'ultimate', 'goal')
('ultimate', 'goal', 'of')
('goal', 'of', 'NLP')
('of', 'NLP', 'is')
('NLP', 'is', 'to')
('is', 'to', 'help')
('to', 'help', 'computers')
('help', 'computers', 'understand')
('computers', 'understand', 'language')
('understand', 'language', 'as')
('language', 'as', 'well')
('as', 'well', 'as')
('well', 'as', 'we')
('as', 'we', 'do')

For sentence 2 , trigrams are: 
('', 'It', 'is')
('It', 'is', 'the')
('is', 'the', 'driving')
('the', 'driving', 'force')
('driving', 'force', 'behind')
('force', 'behind', 'things')
('behind', 'things', 'like')
('things', 'like', 'virtual')
('like', 'virtual', 'assistants,')
('virtual', 'assistants,', 'speech')
('assistants,', 'speech', 'recognition,')
('speech', 'recognition,', 'sentiment')
('recognition,', 'sentiment', 'analysis,')
('sentiment', 'analysis,', 'automatic')
('analysis,', 'automatic', 'text')
('automatic', 'text', 'summarization,')
('text', 'summarization,', 'machine')
('summarization,', 'machine', 'translation')
('machine', 'translation', 'and')
('translation', 'and', 'much')
('and', 'much', 'more')

For sentence 3 , trigrams are: 
('', 'In', 'this')
('In', 'this', 'post,')
('this', 'post,', 'we’ll')
('post,', 'we’ll', 'cover')
('we’ll', 'cover', 'the')
('cover', 'the', 'basics')
('the', 'basics', 'of')
('basics', 'of', 'natural')
('of', 'natural', 'language')
('natural', 'language', 'processing,')
('language', 'processing,', 'dive')
('processing,', 'dive', 'into')
('dive', 'into', 'some')
('into', 'some', 'of')
('some', 'of', 'its')
('of', 'its', 'techniques')
('its', 'techniques', 'and')
('techniques', 'and', 'also')
('and', 'also', 'learn')
('also', 'learn', 'how')
('learn', 'how', 'NLP')
('how', 'NLP', 'has')
('NLP', 'has', 'benefited')
('has', 'benefited', 'from')
('benefited', 'from', 'recent')
('from', 'recent', 'advances')
('recent', 'advances', 'in')
('advances', 'in', 'deep')
('in', 'deep', 'learning')

For sentence 4 , trigrams are: 


Process finished with exit code 0
