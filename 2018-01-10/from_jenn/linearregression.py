#linear regression is a tool we can use to predict the future
#regression is just a certain type of predictors -
#1. for categorical (discrete)data (dog, cat, up, down,True, False)
#2. second type for continuous data (like temperature, housing prices, etc).
#y axis is for what you want to predict (housing price)
#x axis is the predicter or feature (the square footage) as SQFT goes up, so does the price
#simple linear regression uses one feature
#multiple linear regression is choosing multiple features at once
#feature engineering is creating new data from columns you have that
#weren't so good at predicting to someething that is good at predicting
#line (y = mx + b)  y is houseing price, x is SQFT, b is the y incercept  m is the slope of the line
#yhat = betazero + Beta1x1  or predictedy = yintercept + slope(x)

#rsquared is super useful to determine fit for a model 0-1 score
#OLS = ordinary least squares



#confusion matrix    false positives(type1 error) and false negatives(type2 error)
#actual positives are true positive and false negatives
#actual negatives are true negative and false positives

#True Positive Rate (Recall Sensitivity) probability of detection (True Positives/Actual Condition Positive)
#true postitive/true positive + false negatives(type2 errors)

#PPV = Positive Predictive Value or Precision ( true positive/Predicted condition positive)
#true postitive/true positive + false positives(type1 errors)
