create_corrplot=function(data,directory="C:/Users/lukas/Desktop/bachelor/data/figures"){
  cor_matrix=cor(imputed_reduced)
  #fig=corrplot(cor_matrix)
  png("corrplot.png", width = 800, height = 600)
  corrplot(cor_matrix, method = "circle")
  dev.off()
}

