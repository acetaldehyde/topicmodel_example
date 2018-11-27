# トピックモデル生成と分類の例

## 概要

データベースに格納されたテキストデータからトピックモデルを作成し、それらを分類する例。  
`tabledefinition.sql`は例で用いるスキーマ。

## 実行方法

### モデル作成時
引数にトピック数を設定できる。  
python3 make_topicmodel.py 5

### 分類時
データベースのテキストデータを分類する。  
python3 topic_estimation.py