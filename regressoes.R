# SIMPLE AND MULTIPLE LINEAR REGRESSION 

# SIMPLE LINEAR REGRESSION. EXAMPLE 1.

head(cars)
cor(cars)
# R = 0.807 (strong positive correlation. Linear model is therefore applicable)
model = lm(speed ~ dist, data = cars)
plot(speed ~ dist, data = cars)
abline (model)

# what was the corresponding speed for dist = 22?

predict(model,data.frame(dist = 22))
#another option: speed_22 = model$coefficients[1]+22*model$coefficients[2]




# SIMPLE LINEAR REGRESSION. EXAMPLE 2.

head(mtcars)
cor(mtcars[1:4])
model2 = lm(mpg~disp,data=mtcars)
summary(model2)$r.squared
summary(model2)$adj.r.squared
plot(mpg~disp,data = mtcars)
abline(model2)
predict(model2,data.frame(disp=200))




# MULTIPLE LINEAR REGRESSION. EXAMPLE 1.

cor(mtcars[1:4])
model3 = lm(mpg~disp+hp+cyl,data=mtcars)
summary(model3)$r.squared
summary(model3)$adj.r.squared
predict(model3, data.frame(disp=200, hp=100,cyl=4))
