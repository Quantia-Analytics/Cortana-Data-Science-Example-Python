def azureml_main(frame1):
  import milkutilities as mu
 
  numCols = ["Cotagecheese.Prod", "Icecream.Prod", "Milk.Prod", "N.CA.Fat.Price"]
  ## Call the log_cols function in the milkutilities script
  frame1[numCols] = frame1[numCols].apply(mu.log_cols)
  frame1[numCols] = frame1[numCols].apply(lambda df: \
     df.sub(df.mean(1), axis = 0).div(df.std(1), axis = 0))
  return frame1