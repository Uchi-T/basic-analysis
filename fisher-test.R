# 各行に対してFisherの正確確率検定(両側検定)を行う。
# Fisherの正確確率検定は、エンリッチメント解析(例えばDAVID)などで使われる。(DAVIDの場合は片側検定)
# さらに、Benjamini-Hochberg methodによる多重検定補正も行う。
# インプットファイルdara.tsvは、1行目がヘッダ、1列目がIDのタブ区切りテキストファイル。
# 各行において、2x2分割表におけるN11、N12、N21、N22が、2列目~5列目に並んでいる。

# インプットファイルを読み込む。
data <- read.table("data.tsv", header=TRUE, sep="\t")

# Fisherの正確確率検定によって得られるp-valueと、多重検定補正によって得られるq-valueを入れるためのベクトルを作っておく。
pval <- numeric(nrow(data))
qval <- numeric(nrow(data))

# 各行に対してFisherの正確確率検定(両側検定)を行う。
# N11~N22には、それぞれ2~5列目の名前を書き入れる。
for (i in 1:nrow(data)) {
  row <- data[i,]
  a <- row$N11
  b <- row$N12
  c <- row$N21
  d <- row$N22
  mx <- matrix(c(a, b, c, d), nrow=2, byrow=TRUE)
  ft <- fisher.test(mx)$p.value
  pval[i] <- ft
}

# Benjamini-Hochberg method(BH法)でq-valueを計算する。
qval <- p.adjust(pval, method = "BH")

# 結果をファイルに出力する。
# idには、インプットファイルの1列目の名前を書き入れる。
# 1行目がヘッダ、1列目がID、2列目がp-value、3列目がq-valueのファイルが出力される。
result <- data.frame(id=data$id, p_value=pval, q_value=qval)
write.table(result, file="result.tsv", sep="\t", row.names=FALSE)
