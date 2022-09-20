# put your code here. The data frame is already loaded and stored as penguins_df. 

print(penguins_df.loc[penguins_df.species == 'Adelie', 'island':'body_mass_g':2])
