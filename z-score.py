# row z-score を求める。
# 例えば、RNA-seq解析のときに遺伝子発現量を正規化する目的で使う。
# 上記の例の場合、インプットファイルは、1列目が遺伝子名、2列目以降が発現量、1行目がヘッダになっているタブ区切りテキストファイルを想定。
# コマンドラインから、"python3 z-score.py ファイル名"と入力することで実行する。
# z-scoreの定義上、全ての列の値が等しい場合(どの条件でも遺伝子発現量が0のときなど)は計算されない。

import scipy as sp
import pandas as pd
import sys

# 変数fileに上記の"ファイル名"を代入。
file = sys.argv[1]

# データフレームを作成。
df = pd.read_table(file, index_col = 0)
# 行ごとに処理するため、apply関数を使用。z-scoreはscipyの関数を使用して計算。
zs = df.apply(sp.stats.zscore, axis=1)
# タブ区切りテキストとして保存。
zs.to_csv('zscore.tsv',sep = "\t") 
