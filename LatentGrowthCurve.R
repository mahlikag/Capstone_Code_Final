#install.packages("lavaan", dependencies = TRUE)
#install.packages("readxl")
#install.packages("broom")

#loading libraries
library("lavaan")
library("readxl")
library("broom")

#Importing the excel sheets and saving each sheet as a new variable:
for (i in 1:10) {
  assign(paste0("my_data",i),read_excel("Data/2007-2016.xlsx",i))
}

#Storing the important values (indivudal clearance rates, populations, and crime rates) as variables. 
#A new variable is created with respect to the year. 
#I.E: AggravatedAssault1 corresponds to the aggravated assault clearance rate column of the first year

for (i in 1:10) {
  assign(paste0("AggravatedAssault",i),eval(parse(text = paste0("my_data",i)))$`Aggravated Assault Clearance Rate`)
  assign(paste0("Rob",i),eval(parse(text = paste0("my_data",i)))$`Robbery Clearance Rate`)
  assign(paste0("Mrdr",i),eval(parse(text = paste0("my_data",i)))$`Murder/Nonnegligent Manslaughter Clearance Rate`)
  assign(paste0("Pop",i),eval(parse(text = paste0("my_data",i)))$`Total Population`)
  assign(paste0("Cr_rte",i),eval(parse(text = paste0("my_data",i)))$`Crime Rate`)
}


#The following chunk of code stores all of the values we extracte in the preiouvs chunk into a new data frame:
FinalData <- data.frame(aa1=AggravatedAssault1,robbery1=Rob1,murder1=Mrdr1,population1=Pop1,crime_rate1=Cr_rte1,
                        aa2=AggravatedAssault2,robbery2=Rob2,murder2=Mrdr2,population2=Pop2,crime_rate2=Cr_rte2,
                        aa3=AggravatedAssault3,robbery3=Rob3,murder3=Mrdr3,population3=Pop3,crime_rate3=Cr_rte3,
                        aa4=AggravatedAssault4,robbery4=Rob4,murder4=Mrdr4,population4=Pop4,crime_rate4=Cr_rte4,
                        aa5=AggravatedAssault5,robbery5=Rob5,murder5=Mrdr5,population5=Pop5,crime_rate5=Cr_rte5,
                        aa6=AggravatedAssault6,robbery6=Rob6,murder6=Mrdr6,population6=Pop6,crime_rate6=Cr_rte6,
                        aa7=AggravatedAssault7,robbery7=Rob7,murder7=Mrdr7,population7=Pop7,crime_rate7=Cr_rte7,
                        aa8=AggravatedAssault8,robbery8=Rob8,murder8=Mrdr8,population8=Pop8,crime_rate8=Cr_rte8,
                        aa9=AggravatedAssault9,robbery9=Rob9,murder9=Mrdr9,population9=Pop9,crime_rate9=Cr_rte9,
                        aa10=AggravatedAssault10,robbery10=Rob10,murder10=Mrdr10,population10=Pop10,crime_rate10=Cr_rte10
                        
                        )

#The following is the creation of the first model. 
#This model is the latent growth curve model calculation for the Aggravated Assault Clearance Rates. 
#It finds the intercept and slopes using the crime rate and population as time-varying covariates.
model1 <-'
#intercept and slope with fixed coefficients
i=~ 1*aa1 + 1*aa2 + 1*aa3 + 1*aa4 + 1*aa5 + 1*aa6 + 1*aa7 + 1*aa8 + 1*aa9 + 1*aa10 
s=~ 0*aa1 + 1*aa2 + 2*aa3 + 3*aa4 + 4*aa5 + 5*aa6 + 6*aa7 + 7*aa8 + 8*aa9 + 9*aa10
q=~ 0*aa1 + 1*aa2 + 4*aa3 + 9*aa4 + 16*aa5 + 25*aa6 + 36*aa7 + 49*aa8 + 64*aa9 + 81*aa10

#time-varying covariates
aa1 ~ population1 + crime_rate1
aa2 ~ population2 + crime_rate2
aa3 ~ population3 + crime_rate3
aa4 ~ population4 + crime_rate4
aa5 ~ population5 + crime_rate5
aa6 ~ population6 + crime_rate6
aa7 ~ population7 + crime_rate7
aa8 ~ population8 + crime_rate8
aa9 ~ population9 + crime_rate9
aa10 ~ population10 + crime_rate10
'

#The following is the summary statistics of the model we just developed for the Aggravated Assault incidents:
fit1 <- growth(model1,data = FinalData)
summary(fit1)

#The following is the creation of the second model. 
#This model is the latent growth curve model calculation for the Robbery Clearance Rates. 
#It finds the intercept and slopes using the crime rate and population as time-varying covariates.

model2 <-'
#intercept and slope with fixed coefficients
i=~ 1*robbery1 + 1*robbery2 + 1*robbery3 + 1*robbery4 + 1*robbery5 + 1*robbery6 + 1*robbery7 + 1*robbery8 + 1*robbery9 + 1*robbery10 
s=~ 0*robbery1 + 1*robbery2 + 2*robbery3 + 3*robbery4 + 4*robbery5 + 5*robbery6 + 6*robbery7 + 7*robbery8 + 8*robbery9 + 9*robbery10
q=~ 0*robbery1 + 1*robbery2 + 4*robbery3 + 9*robbery4 + 16*robbery5 + 25*robbery6 + 36*robbery7 + 49*robbery8 + 64*robbery9 + 81*robbery10
#regressions
#i ~ x1 + x2
#s ~ x1 + x2
#time-varying covariates
robbery1 ~ population1 + crime_rate1
robbery2 ~ population2 + crime_rate2
robbery3 ~ population3 + crime_rate3
robbery4 ~ population4 + crime_rate4
robbery5 ~ population5 + crime_rate5
robbery6 ~ population6 + crime_rate6
robbery7 ~ population7 + crime_rate7
robbery8 ~ population8 + crime_rate8
robbery9 ~ population9 + crime_rate9
robbery10 ~ population10 + crime_rate10
'
#The following is the summary statistics of the model we just developed for the Robbery incidents.

fit2 <- growth(model2,data = FinalData)
summary(fit2)

#The following stores all of the coefficients we found in the previous modelings:

i1 = coef(fit1)[37] #aggravated assault intercept
s1 = coef(fit1)[38] #aggravated assault linear slope
q1 = coef(fit1)[39] #aggravated assault quadratic slope

i2 = coef(fit2)[37] #robbery intercept
s2 = coef(fit2)[38] #robbery linear slope
q2 = coef(fit2)[39] #robbery quadratic slope

#The following is the plot created from the intercepts and slopes we previously found:

plot.new()
eq = "Latent Growth Curve Model" #Title

#Aggravated Assault Equation
curve(main = eq,q1 * x^2 + s1 * x + i1, xlim = c(0.4,10), ylim = c(0.4,100), lwd = 2,xlab="Years (2007 - 2016)", ylab="Clearance Rate (%)",col='blue')

#Robbery Equation
curve(q2 * x^2 + s2 * x + i2, add = TRUE, col = "red")

#The creation of the legend 
legend(6, 100, legend=c("Aggravated Assault", "Robbery"),
       col=c("blue", "red"), lty=1, cex=0.8)
