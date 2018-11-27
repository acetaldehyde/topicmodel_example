#トピックモデルを作成する

from janome.tokenizer import Tokenizer
import mysql.connector
from pprint import pprint
import gensim
from gensim import corpora
import sys

DICT_FILE_NAME = './datas/posts.dict.dict'
DICT_TEXT_FILE_NAME = './datas/posts.dict.txt'
CORPUS_FILE_NAME = './datas/posts.corpus.mm'
LDA_MODEL_FILE_NAME = './datas/posts.lda'

#名詞を取得する
def get_nouns(text):
    t = Tokenizer()
    terms = [token.surface for token in t.tokenize(text) if token.part_of_speech.startswith('名詞')]
    return terms

#トピック数を指定
args = sys.argv
if args[1]:
    num_topics = int(args[1])
else:
    #default is 5 topics
    num_topics = 5

#get posts
conn = mysql.connector.connect(
    host = '127.0.0.1',
    port = 23306,
    user = 'root',
    password = 'root',
    database = 'termranking',
    buffered = True
)
cursor = conn.cursor(dictionary=True)
get_query = "SELECT text FROM posts limit 1000"
cursor.execute(get_query)
rows = cursor.fetchall()

#ディクショナリーとコーパスを作成
dictionary = corpora.Dictionary([])
corpus = []

for row in rows:
    nouns = get_nouns(row['text'])
    print(nouns)
    #merge dictionary
    new_dictionary = corpora.Dictionary([nouns])
    print(new_dictionary)
    dictionary.merge_with(new_dictionary)
    #merge corpus
    corpus.extend([dictionary.doc2bow(nouns)])

dictionary.save_as_text(DICT_TEXT_FILE_NAME)
dictionary.save(DICT_FILE_NAME)
corpora.MmCorpus.serialize(CORPUS_FILE_NAME, corpus)

#LDAトピックモデルを作成
lda = gensim.models.ldamodel.LdaModel(
    corpus=corpus,
    num_topics=num_topics,
    id2word=dictionary
)
lda.save(LDA_MODEL_FILE_NAME)
pprint(lda.show_topics())

cursor.close()
conn.close()