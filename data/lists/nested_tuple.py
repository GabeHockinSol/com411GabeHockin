# stores "all_steps" in a tuple so we can call them in function for later use
def steps():
  all_steps = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return all_steps

# calls steps
def run():
  all_steps = steps()
  good_steps = []
  bad_steps = []
  
  # does a check to find which steps from the tuple are greate than or equal to
  for step in all_steps:
    if (step[1] >= 50):
      bad_steps.append(step)
    else:
      good_steps.append(step) 

# print calculations to log
  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

# calls run
run()