def check_gryffindor_eligibility(bravery, loyalty, ambition):
    """
    Given three integer scores (0-10) for bravery, loyalty and ambition,
    decide whether a student is Gryffindor material.

    Rules:
    - Every score must be between 0 and 10 (inclusive). If any score is
      out of that range, return "Invalid score".
    - The student qualifies if bravery is at least 7, AND at least one
      of loyalty or ambition is at least 5.
    - If they qualify, return "Gryffindor materi_al!".
    - If they do not qualify, return "Not Gryffindor material.".
    """
    
    #checking within boundaries
    valid_inputs = True
    eligible = True
    if bravery > 10 or bravery < 0:
      valid_inputs = False
    elif loyalty > 10 or loyalty < 0:
      valid_inputs = False
    elif ambition > 10 or ambition < 0:
      valid_inputs = False
      
    #now checking for fail conditions
    #high bravery, low loyalty / ambition
    if valid_inputs == True and bravery >= 7 and (loyalty < 5 or ambition < 5):
      eligible = False
    #low bravery, high others
    elif valid_inputs == True and bravery < 7 and  (loyalty >= 5 or ambition >= 5):
      eligible = False
    #low everything
    elif valid_inputs == True and bravery < 7 and (loyalty < 5 or ambition < 5):
      eligible = False
      
    #finally, succeeding
    if valid_inputs == True and bravery >= 7 and (loyalty >=5 or ambition >= 5):
      eligible = True
      
    #then, determining output
    if valid_inputs == False:
      return("Invalid score")
    elif valid_inputs == True and eligible == False:
      return("Not Gryffindor material.")
    elif valid_inputs == True and eligible == True:
      return("Gryffindor material!")
    else:
      return("Invalid score")
      
    
    
    


