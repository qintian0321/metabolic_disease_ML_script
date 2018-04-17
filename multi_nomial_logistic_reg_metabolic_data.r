read.csv("",header=T,row.names=1)->metab

Labels2<-rep(0,dim(metab)[1])

Labels2 [which(metab$Label==1)]<-"GA1"
Labels2 [which(metab$Label==2)]<-"MMA"
Labels2 [which(metab$Label==3)]<-"OTCD"
Labels2 [which(metab$Label==4)]<-"VLCADD"
Labels2 [which(metab$Label==0)]<-"CONTROL"
factor(Labels2)->metab$Labels2
metab$Labels3 <- relevel(metab$Labels2, ref = "CONTROL")
test <- multinom(metab$Labels3 ~ as.matrix(metab[,c(1:46)]),maxit=1000)
test <- multinom(metab$Labels3 ~ as.matrix(metab[,c(1:46)])*as.matrix(metab[,51]),maxit=1000)

cbind(as.matrix(predict(test,newdata=as.matrix(metab[,c(1:46)]))),as.matrix(metab$Labels3))