# グループごとの平均値を計算する、という操作を行ごとに繰り返す。
# 例えば、それぞれn個体ずつ使用してm通りの条件で実験を行い、各個体の遺伝子発現量を算出したあと、条件ごとの発現量の平均値を求めるような場合に使う。
# インプットは1列目が遺伝子名、2列目以降が発現量、1行目がヘッダとなっているファイルを想定。
# インプットファイルでは、「遺伝子名, 条件A-個体1, 条件A-個体2, 条件A-個体3, 条件B-個体1, 条件B-個体2,...」のような順で数値が並んでいる。
# コマンドラインから、"python3 multi-average.py ファイル名 mの値 nの値 出力ファイル名"と入力して実行。


import pandas as pd
import sys

# 変数fileに上記の"ファイル名"を代入。
file = sys.argv[1]
# 変数mに上記の"m"を代入。コマンドラインから入力した字を「文字列str」から「整数int」に変換。
m = int(sys.argv[2]) 
# 変数nに上記の"n"を代入。コマンドラインから入力した字を「文字列str」から「整数int」に変換。
n = int(sys.argv[3])
# 変数outに上記の"出力ファイルの名前"を代入。
out = sys.argv[4]

# インプットファイルを読み込んでデータフレームに入れる。
df = pd.read_table("tpm.tmm-normalized2.txt",index_col=0)

# インデックスだけdfと同じものを確保し、それ以外は空のデータフレームを用意。
avg = pd.DataFrame(index=df.index, columns=[])

# avgに新たな条件の平均値を追加していく。
for i in range(1, m+1):
    avg = pd.concat([avg, df.iloc[:, 0+n*(i-1):n+n*(i-1)].mean(axis=1)],axis=1)
    # iloc[]でdfから特定の範囲を取り出す。
    # mean(axis=1)で平均値を出す。axis=1によって列ではなく行の平均であることを指定。
    # concatでavgに新たな条件の平均値を結合。axis=1によって縦ではなく横に結合することを指定。
    
avg.to_csv(out, sep="\t") # タブ区切りテキストとして保存。
