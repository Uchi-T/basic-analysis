#row z-score を求める。
#RNA-seq解析の遺伝子発現量を正規化する目的で、1列目が遺伝子名、1行目が実験条件等になっているタブ区切りファイルを使うことを想定。
#コマンドラインから、"python3 z-score.py ファイル名 インデックスにする列の名前(geneIDなど)"と入力することで実行。

import scipy as sp #科学技術系の解析に強いライブラリ。
import pandas as pd #データ解析用ライブラリ。表形式に強い。
import sys

file = sys.argv[1] #sys.argvはコマンドライン引数のリスト。sys.argv[1]は上記の"ファイル名"にあたる。
index = sys.argv[2]

df = pd.read_table(file, index_col = index) #データフレームを作成。
zs = df.apply(sp.stats.zscore, axis=1) #行ごとに処理するため、apply関数を使用。z-scoreはscipyの関数を使用して計算。
zs.to_csv('zscore.tsv',sep = "\t") #タブ区切りテキストとして保存。

#z-scoreの定義上、全ての値が同じ場合は計算されない。
    
    
