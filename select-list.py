# リストとファイルを比較して、ファイルの中からリストの条件に一致する行を取ってくる。
# 例えば、遺伝子発現量の表(ファイル)から、DEGs(リスト)の発現量だけを取ってくるときに使う。
# インプットファイルは「ファイル」と「リスト」の二つ。
# 「ファイル」は1列目が遺伝子名、2列目以降が発現量、1行目がヘッダとなっているものを想定。

# コマンドラインから、"python3 select-list1.py ファイル名 リスト名 出力ファイル名"と入力して実行。


import pandas as pd
import sys

# 変数fileに上記の"ファイル名"を代入。
file = sys.argv[1]
# 変数lstに上記の"リスト名"を代入。
lst = sys.argv[2]
# 変数outに上記の"出力ファイルの名前"を代入。
out = sys.argv[3]

# ファイルを読み込んでデータフレームに入れる。
df = pd.read_table(file)
# リストを読み込んでデータフレームに入れる。
ls = pd.read_table(lst, header=None)

#表の中からリストと一致する行だけを抽出。
selected = df[df[df.columns[0]].isin(ls[0])]
# df.columns[0]で1列目の列名を取ってくる。
# df[df.columns[0]]で1列目の値を取ってくる。
# isin(ls[0])でdf[df.columns[0]]の遺伝子がリストの中に存在するかチェック。存在する場合はTrue、しない場合はFalseを返す。

# タブ区切りテキストとして保存。
selected.to_csv(out, sep="\t", index=False) 
