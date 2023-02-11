# リストとファイルを比較して、ファイルの中からリストの条件に一致する行を取ってくる。
# 例えば、遺伝子発現量の表から、DEGのリストにある遺伝子の発現量だけを取ってくるときに使う。
# インプットファイルは「ファイル」と「リスト」の二つ。
# 「ファイル」は1列目が遺伝子名、2列目以降が発現量、1行目がヘッダとなっているものを想定。

# コマンドラインから、"python3 select-list1.py ファイル名 リスト名 出力ファイル名"と入力して実行。


import pandas as pd
import sys

file = sys.argv[1] # 上記の"ファイル名"。
lst = sys.argv[2] # 上記の"リスト名"。
out = sys.argv[3] # 上記の"出力ファイルの名前"

df = pd.read_table(file) # ファイルを読み込んでデータフレームに入れる。
ls = pd.read_table(lst, header=None) # リストを読み込んでデータフレームに入れる。

selected = df[df[df.columns[0]].isin(ls[0])] #表の中からリストと一致する行だけを抽出。
# df.columns[0]で1列目の列名を取ってくる。
# df[df.columns[0]]で1列目の値を取ってくる。
# isin(ls[0])でdf[df.columns[0]]の遺伝子がリストの中に存在するかチェック。存在する場合はTrue、しない場合はFalseを返す。

selected.to_csv(out, sep="\t", index=False) # タブ区切りテキストとして保存。
