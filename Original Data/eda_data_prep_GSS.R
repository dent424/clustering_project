setwd("C:/Clustering Project/data")
GSS <- read.csv('GSS_comma.csv')
summary(GSS)
keep_vars=c("year","id_","age","sex","race","polviews","natspac","natcity",
            "natcrime","natdrug","nateduc","natrace","natarms",
            "nataid","natfare","natroad","natsoc","natpark","natchld",
            "natsci","natenrgy","natspacy","natenviy","nathealy",
            "natcityy","natcrimy","natdrugy","nateducy", "natracey",
            "natarmsy","nataidy","natfarey", "confinan","conbus",
            "toofast","gwsci","gwpol","gwbiz","sciagrgw","sciinfgw","polinfgw",
            "bizinfgw","scibstgw","polbstgw","bizbstgw","ecoagree","ecobsttx",
            "bizbsttx","polbsttx","extinct","sealevel","penguins","inuitway",
            "noicecap","intintl","intecon","intenvir","morempg",
            "privent","harmgood","scigrn",
            "grnecon","harmsgrn","grnprog","grwthelp",
            "grwtharm","grnprice","grntaxes","grnsol","toodifme",
            "ihlpgrn","carsgen","nukegen","indusgen","chemgen","watergen","usdoenuf",
            "recycle","chemfree","drivless","popgrwth",
            "impgrn","othssame","grnexagg","grnintl","ldcgrn",
            "econgrn","grncon","knwcause","knowsol","helpharm",
            "grneffme", "tempgen1", "redcehme", "h2oless","nobuygrn","govdook","polgreed")

cluster_vars=c("polviews","toofast")

reduced = GSS[keep_vars]


i=1
while(i < length(keep_vars)-1)
  {
    i = i+1
    j = i+1
    reduced[,j]<- ifelse(reduced[,j] == "Agree", 4,
        ifelse(reduced[,j] == "Disagree", 2,
        ifelse(reduced[,j] == "Neither agree nor disagree", 3,
        ifelse(reduced[,j] == "Strongly agree", 5,
        ifelse(reduced[,j] == "Strongly disagree", 1,
        ifelse(reduced[,j] == "Agree strongly", 5,
        ifelse(reduced[,j] == "Disagree strongly", 1,
        ifelse(reduced[,j] == "Always", 4,
        ifelse(reduced[,j] == "Often", 3,
        ifelse(reduced[,j] == "Sometimes", 2,
        ifelse(reduced[,j] == "Never", 1,
        ifelse(reduced[,j] == "Fairly willing", 4,
        ifelse(reduced[,j] == "Neither willing nor unwill", 3,
        ifelse(reduced[,j] == "Not at all willing", 1,
        ifelse(reduced[,j] == "Not very willing", 2,
        ifelse(reduced[,j] == "Very willing", 5,
        ifelse(reduced[,j] == 2, 2,
        ifelse(reduced[,j] == 3, 3,
        ifelse(reduced[,j] == 4, 4,
        ifelse(reduced[,j] == "Not at all concerned", 1,
        ifelse(reduced[,j] == "Very concerned", 5,
        ifelse(reduced[,j] == "Know a great deal", 5,
        ifelse(reduced[,j] == "Know nothing at all", 1,
        ifelse(reduced[,j] == "Extremely dangerous for the environment", 5,
        ifelse(reduced[,j] == "Not dangerous at all for the environment?", 1,
        ifelse(reduced[,j] == "Not very dangerous, or", 2,     
        ifelse(reduced[,j] == "Somewhat dangerous", 3,
        ifelse(reduced[,j] == "Very dangerous", 4,
        ifelse(reduced[,j] == "Conservative", 2, 
        ifelse(reduced[,j] == "Extremely liberal", 7 ,        
        ifelse(reduced[,j] == "Extrmly conservative", 1,        
        ifelse(reduced[,j] == "Liberal", 6,        
        ifelse(reduced[,j] == "Moderate", 4,        
        ifelse(reduced[,j] == "Slightly conservative", 3,        
        ifelse(reduced[,j] == "Slightly liberal", 5 ,        
        ifelse(reduced[,j] == "", , 
        ifelse(reduced[,j] == "", ,        
        ifelse(reduced[,j] == "", ,        
        ifelse(reduced[,j] == "", ,        
        ifelse(reduced[,j] == "", ,        
        ifelse(reduced[,j] == "", ,        
        ifelse(reduced[,j] == "", ,               
               NA))))))))))))))))))))))))))))
}



