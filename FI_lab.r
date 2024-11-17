library(data.table)
file<-list.files(pattern="Item_")
lab<-read.csv("lab.csv",header=T,stringsAsFactors=FALSE,)
drug<-as.data.frame(fread("/home/mw/input/csv15153/mimiciv_hosp.diagnoses_icd.csv",header=T,stringsAsFactors=FALSE,na.strings=""))
le<-as.data.frame(fread(file[1],header=T,stringsAsFactors=FALSE,na.strings=""))
for(i in 2:length(file)){
	tmp<-as.data.frame(fread(file[i],header=T,stringsAsFactors=FALSE,na.strings=""))
	le<-rbind(le,tmp)
}
le$hadm_id<-NULL
le_sub<-le[le$subject_id %in% lab$subject_id,]
le_sub<-na.omit(le_sub)
le_sub$score<-1
#正常打0
le_sub[le_sub$valuenum < le_sub$ref_range_upper & le_sub$valuenum > le_sub$ref_range_lower,"score"]<-0
score<-table(le_sub$subject_id,le_sub$score)[,2]/length(names(table(le$itemid)))
dat<-data.frame(subject_id=names(score),FI_lab_score=score)
