# Documentation for OOP of my dev project.

- Creator Class
    - Attributes:
        - char_inputs (dict). This is the dictionary that holds all different possible choices for a person's character.
        - screen (operator). This assigns Screen() from turtle into the class so that questions can be inputted using the turtle interafce.
    
    - Methods (I'm still deciding if I should split the methods into a separate class from the Creator Class):
        - In addition, I'm still deciding on whether to split out the questions (user inputs) passed into the class as attributes, or keep them within the method when they show up.

        - name(): Returns a first and last name for the player based on random
        letters chosen from inputs.
        
        - region(): Returns user's choice of region for their character
        
        - planet(region_choice): 
            - Parameter region_choice (str): returns the user's region choice that was made in the region() function.
            - Returns the player's origin planet based on their region choice.
        
        - species(region_choice): 
            - Parameter region_choice (str): returns the user's region choice that was made in the region() function.
            - Returns the player's species based on their region choice.
        
        - current_sit(): Returns the player's current situation based on their allegiance
        
        - appearance(): Returns the player's physical appearance based on inputted age.

- Abilities Class
    - (Again same issue of possibly too many methods in one class, but I'm still testing different combinations to see if I can make it simpler)
    
    - Attributes:
        - attributes (dict): This is a dictionary taht holds each ability/skill as well as the point value associated with it. Follows similar format to Dungeons and Dragons.
    
    - Methods:
        - set_difficulty(): Returns starting modifier score based on choice of difficulty made.
        
        - user_check(self, points_spent): 
            - Parameter points_spent(int): passes in the deducted points from the add_points()
            - Checks if all points are spent. Returns True if user
        accepts point allocation, or restarts add_points() if False.
        
        - add_points(): Allocates points to the values key in the attributes dictionary
        for each specific attribute.
        
        - modifier_creator(self, start_modifier): 
            - Parameter start_modifier(int): the returned value of set_difficulty().
            - Creates a new dictionary key for the modifier, adjusts the modifier
        score depending on the values assigned for each attribute.
        
        - add_modifier(): Returns a combined modifier score for each attribute.
    