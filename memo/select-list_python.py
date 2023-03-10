# リストとファイルを比較して、ファイルの中からリストに一致する行を取ってくる。
# 例えば、RNA-seqで得られた遺伝子発現量の表の中から、DEGのリストに含まれる遺伝子の情報を取ってくる時に使う。
# 上記の例の場合、1列目がgeneID、2列目以降が発現量、1行目がヘッダとなっているファイルをインプットファイルとする。
# 実用的なのは一番下のisin()を使う方法。


import pandas as pd

file = "ファイル名"
df = pd.read_table(file) # ファイルを読み込む

lst = "リスト名"
ls = pd.read_table(lst,header=None) # リストを読み込む


###############特定の1つの遺伝子の発現量を抽出###############
df[df["geneID"] == ls.at[0,0]]


###############リストにある全ての遺伝子を検索###############
slct = df[df["geneID"] == ls.at[0,0]] # まずリストの一番目に一致する行を取ってきてデータフレームにする。
for i in range(1,len(ls)):
    match = df[df["geneID"] == ls.at[i,0]]
    slct = pd.concat([slct,match], axis = 0) # 最初に作ったデータフレームに順次追加していく。

# リストの１番目にマッチする行が表形式ファイル内に存在することを前提としている。


###############リストにある全ての遺伝子を検索・isin()を使ってスマートに###############
selected = df[df[df.columns[0]].isin(ls[0])]
# df.columns[0]で1列目の列名を取ってくる。
# df[df.columns[0]]で1列目の値を取ってくる。
# isin(ls[0])でdf[df.columns[0]]の遺伝子がリストの中に存在するかチェック。存在する場合はTrue、しない場合はFalseを返す。
# df[]でTrueの遺伝子だけを取ってくる。
