# simple-python-social-network
Simple social network program to practice with Lists, Nested lists, Dictionaries, Functions.

## Description
A simple approach to suggest the most probable new friend for users on a social network such as Facebook.

The algorithm begins with: for each user go through all the other users (another “for”) and calculate
the number of friends they have in common. Then for a given user the friend you will suggest to them
is the user in the social network who they are currently not friends with, but have the most friends in
common. Intuitively, it makes sense why they might want to be connected as friends. (Note that
when you look for your most common friend in this scheme, it will be you, i.e. you will have to
remember to remove yourself from consideration.) 
