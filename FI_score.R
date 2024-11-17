data<-readRDS("/home/mw/input/merge_data3639/merge_cleaned.rds")
FI_index<-data[,c(1,2,6,17:33,35,38,49)]
feature_index<-data[,-c(3:8,14,15,17:33,35:38,49,52:54)]
FI_train<-FI_index[which(data$anchor_year_group %in% unique(data$anchor_year_group)[-3]),]
FI_test<-FI_index[which(data$anchor_year_group %in% unique(data$anchor_year_group)[3]),]
prerisk_train<-feature_index[which(data$anchor_year_group %in% unique(data$anchor_year_group)[-3]),]
prerisk_test<-feature_index[which(data$anchor_year_group %in% unique(data$anchor_year_group)[3]),]
FI_index[which(FI_index$age>59),'elder']<-1
FI_index[which(FI_index$gcs_score<9),'gcs_level']<-1
FI_index[which(FI_index$gcs_score>8 & FI_index$gcs_score<14),'gcs_level']<-0.5
FI_index[which(FI_index$sapsii>26),'sapsii_level']<-1
FI_index[which(FI_index$sapsii>13 & FI_index$sapsii<27),'sapsii_level']<-0.5
FI_index[which(FI_index$sapsii<14),'sapsii_level']<-0
FI_index[,'FI_score']<-apply(FI_index[,c(4:17,20,24:26)],1,sum)/length(colnames(FI_index)[c(4:17,20,24:26)])
FI_train<-FI_index[which(data$anchor_year_group %in% unique(data$anchor_year_group)[-3]),c(1:2,27)]
fwrite(FI_train,file='FI_train.csv',row.names=F,col.names=T,quote=F)
FI_test<-FI_index[which(data$anchor_year_group %in% unique(data$anchor_year_group)[3]),c(1:2,27)]
fwrite(FI_train,file='FI_test.csv',row.names=F,col.names=T,quote=F)
fwrite(FI_index,file='FI_socre.csv',row.names=F,col.names=T,quote=F)
feature_train[1:2,]
fwrite(prerisk_train,file='feature_train.csv',row.names=F,col.names=T,quote=F)
fwrite(prerisk_test,file='feature_test.csv',row.names=F,col.names=T,quote=F)
fwrite(feature_index,file='feature_data.csv',row.names=F,col.names=T,quote=F)