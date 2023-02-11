# python3でrow z-scoreを求める方法を検討した。実用的なのは一番下のPandasを使う方法。
# RNA-seq解析で得られた遺伝子発現量を正規化することを想定。


import numpy as np
# numpyは多次元配列の扱いを効率化するライブラリ。標準ライブラリではないので、入っていなければインストールしておく。
# 名前を簡略化するため、"np"としてインポート。
import scipy as sp
# scipiは科学技術系の計算用のライブラリ。
import pandas as pd
# pandasはデータ解析用ライブラリ。ヘッダのついたcsvファイルなど表形式を扱いやすい。


# テスト用データ(1行のみ)
data = ([5, 8, 2, 10, 14])

################ 1行のみの場合・自力で計算 ################

d = np.array(data) #"np."は、npというライブラリを使うという意味。arrayは関数名。
avg = np.mean(d) #　平均
std = np.std(d) #　標準偏差
zscore = (d-np.mean(d))/np.std(d)


################ 1行のみの場合・scipiの関数を使って計算 ################
d = np.array(data)
zscore = sp.stats.zscore(d)



# テスト用データ(複数行)
data = ([5, 8, 2, 10, 14],[2,2,5,7,12],[3,5,1,0,8])

################ 複数行の場合・numpyを使う ################
d = np.array(data) #numpyの性質上、列名・行名をつけたまま扱えない。
zscore = np.empty((d.shape[0], d.shape[1])) #　dataと同じ行数・列数の空の配列を作成。
for i in range(0,d.shape[0]):
    zscore[i] = sp.stats.zscore(d[i]) #　空の配列の各行をz-scoreで置き換えていく。


################ タブ区切りファイルを読み込む場合・pandasを使う ################

#　fileはファイル名。
df = pd.read_table(file, index_col = 0) #　データフレームを作成。
zs = df.apply(sp.stats.zscore, axis=1) #　行ごとに処理するため、apply関数を使用。z-scoreはscipiの関数を使用。
zs.to_csv('zscore.tsv',sep = "\t") #　タブ区切りテキストとして保存。

#　z-scoreの定義上、全ての値が等しい行では結果が出力されない。
