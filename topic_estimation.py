from janome.tokenizer import Tokenizer
import mysql.connector
from pprint import pprint
import gensim
from gensim import corpora
import sys

LDA_MODEL_FILE_NAME = './datas/posts.lda'
DICT_FILE_NAME = './datas/posts.dict.dict'

#名詞を取得する
def get_nouns(text):
    t = Tokenizer()
    terms = [token.surface for token in t.tokenize(text) if token.part_of_speech.startswith('名詞')]
    return terms

def get_topic_number(corpus):
    lda = gensim.models.ldamodel.LdaModel.load(LDA_MODEL_FILE_NAME)
    
    topic_number = 0
    max_score = 0
    for topics_per_document in lda[corpus]:
        for topics in topics_per_document:
            pprint(topics)
            if max_score < topics[1]:
                topic_number = topics[0]
                max_score = topics[1]
                
    exit()
    return topic_number
    
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
get_query = "SELECT id, text FROM posts limit 1000"
cursor.execute(get_query)
rows = cursor.fetchall()

dictionary = corpora.Dictionary.load(DICT_FILE_NAME)

#トピックテーブルをtruncate
cursor.execute('TRUNCATE TABLE topics');

for row in rows:
    nouns = get_nouns(row['text'])
    texts = [nouns]
    corpus = [dictionary.doc2bow(nouns)]
    pprint(corpus)
    topic_number = get_topic_number(corpus)
    print("Topic number is {}".format(topic_number))
    
    #insert
    insert_query = "INSERT INTO topics (post_id, topic_number) VALUES ('{}', {})".format(row['id'], topic_number)
    cursor.execute(insert_query);
    
conn.commit()
cursor.close()
conn.close()