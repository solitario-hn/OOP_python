# df1 = pandas.DataFrame({"name": ["Alice"], "age": [25]})  # index: [0]
# df2 = pandas.DataFrame({"name": ["Bob"], "age": [30]})    # index: [0]

# Without ignore_index:
#result = pandas.concat([df1, df2])
# Creates:  name   age
#       0   Alice  25
#       0   Bob    30    <- Duplicate index!

# With ignore_index=True:
#result = pandas.concat([df1, df2], ignore_index=True)
# Creates:  name   age
#       0   Alice  25
#       1   Bob    30    <- Clean sequential index


# # Without index_col:
# df = pandas.read_csv("data.txt")
# # Creates:  Unnamed: 0    website    Email    Password
# #           0             google     john@    pass123
# #           1             facebook   jane@    abc456

# # With index_col=0:
# df = pandas.read_csv("data.txt", index_col=0)  
# # Creates:  website    Email    Password
# #           google     john@    pass123
# #           facebook   jane@    abc456

































window.mainloop()

