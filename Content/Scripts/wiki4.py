from gensim.models import word2vec
model = word2vec.Word2Vec.load("espanol5.model")
print("好きなスペイン語の単語を入力してください。コサイン類似度が高い順に表示します。")
xxx = input()
print(xxx,"が入力されました。")
ret = model.wv.most_similar(positive = xxx ) 


for item in ret:
    print(item[0], item[1])
