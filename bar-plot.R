# グループごとに平均値と標準誤差を計算し、エラーバー付きの棒グラフを作成する。これを各行に対して繰り返す。
# 棒グラフをたくさん作る時に使う。
# インプットファイルは、1列目がIDのタブ区切りテキストファイル。ヘッダはなし。
# 例えば、RNA-seq解析において、各遺伝子で条件ごとに遺伝子発現量の平均を求めて棒グラフにする場合に使う。その場合、1列目が遺伝子名、2列目が個体1の条件A、3列目が個体1の条件B...のような形式のインプットファイル。

library(ggplot2)
library(tidyr)
library(dplyr)

# データを読み込む。
data <- read.table("data.txt", header=FALSE)
# 列の名称を変更する。
# この場合、インプットファイルの1列目がgeneID、2~4列目が個体1の組織A~C、5~7列目が個体2の組織A~C、8~10列目が個体3の組織A~C。
colnames(data) <- c("geneID", "ind1_A", "ind1_B", "ind1_C", "ind2_A", "ind2_B", "ind2_C", "ind3_A", "ind3_B", "ind3_C")


# 各遺伝子の棒グラフを作成する関数を定義する。
plot_gene <- function(gene_id) {

# geneIDがgene_idに一致する行のデータを抽出し、変数data_geneに代入する。
data_gene <- data[data$gene == gene_id, ]
# データの形式を変える。
data_long <- data_gene %>% gather(ind_tissue, expression, -geneID)
# 個体の情報と組織の情報を分割する。
data_long <- data_long %>% separate(ind_tissue, into=c("individual", "tissue"), sep="_")
# 組織ごとの平均値と標準誤差を計算する。
means <- data_long %>% group_by(tissue) %>% summarize(mean=mean(expression), se=sd(expression)/sqrt(length(expression)))
# 出力される棒グラフの順番が入れ替わらないように、順番を指定。(そのままだと組織の順番が入れ替わってしまう)
means <- transform(means, tissue= factor(tissue, levels = c("A", "B", "C")))

# エラーバー付きの棒グラフを作成。
p <- ggplot(means, aes(x=tissue, y=mean))
p <- p + geom_bar(stat="identity", position=position_dodge(), width=0.7)
p <- p + geom_errorbar(aes(ymin=mean-se, ymax=mean+se), width=0.2, position=position_dodge(0.7)) 

# グラフの見た目を整える。
# この場合、x軸の名前は"Tissue"、y軸の名前は"expression level"、グラフのタイトルはgene_id
p <- p + labs(x="Tissue", y="expression level", fill="Region", title=gene_id)
p <- p + theme_bw()
p <- p + theme(panel.grid.major=element_blank(), panel.grid.minor=element_blank(),
      		panel.border=element_blank(), axis.line=element_line(colour="black"),
      		plot.title=element_text(hjust = 0.5, size=10), 
      		axis.title.x=element_text(size=8), axis.title.y=element_text(size=8) )
return(p)
}


# 各遺伝子に対して、上記の関数を適用していく。
gene_list <- unique(data$geneID)
for (gene in gene_list) {
	p <- plot_gene(gene)
  # "遺伝子名.png"という名称のファイルとして保存する。
	ggsave(paste0(gene, ".png"), p, dpi=300, width=2, height=2)
}
