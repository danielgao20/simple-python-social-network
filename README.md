# simple-social-network
Practice with Lists, Nested lists, Dictionaries, Functions.

## Description
A simple approach to suggest the most probable new friend for users on a social network such as Facebook.

The algorithm begins with: for each user go through all the other users (another “for”) and calculate
the number of friends they have in common. Then for a given user the friend you will suggest to them
is the user in the social network who they are currently not friends with, but have the most friends in
common. Intuitively, it makes sense why they might want to be connected as friends. (Note that
when you look for your most common friend in this scheme, it will be you, i.e. you will have to
remember to remove yourself from consideration.) 

## Functions

open_file: prompts the user to enter a file name.

create_network: takes a file pointer, reads the first line to get the number of users, creates a dictionary where each user id corresponds to a list of its friends' ids, populates the dictionary with friend connections from the remaining lines of the file, and returns the resulting network dictionary.

init_matrix: receives a size and creates an n by n matrix, initialized with zeros, and returns the matrix.

common_degree: takes two lists as input, iterates over the items of the first list and checks whether each item is also in the second list, and then returns an integer that represents the number of items that are common to both input lists.

calc_similarity_scores: takes a network dictionary as input, initializes an n x n list of lists with zeros using the init_matrix function, iterates over all pairs of users in the network using nested for loops, obtains the list of friends for each pair of users from the network dictionary, calls the common_degree function to calculate the number of friends they have in common, and stores the resulting degree value in the appropriate locations in the similarity_matrix list of lists, and finally returns the similarity_matrix.

recommend: takes a member_id as input and uses it as an index in the network dictionary and the similarity_matrix to access the list of friends and similarity scores for that user (member_id) with all other users. It then determines the largest value in this list (excluding any user who is already a friend or the member_id itself) and returns the index of the most similar user (i.e., the user with the highest similarity score), which means they have the most friends in common with the member_id.

main: opens a file, creates a social network dictionary using the create_network function, calculates similarity scores between users using calc_similarity_scores, prompts the user for a member_id and validates that the input is within range, uses the recommend function to suggest a friend for the specified member_id, displays the suggestion, and prompts the user to input another member_id or exit.

## Sample Output

Given the following network (small_network_data.txt):
```
0 : [1, 2, 3]
1 : [0, 4, 6, 7, 9]
2 : [0, 3, 6, 8, 9]
3 : [0, 2, 8, 9]
4 : [1, 6, 7, 8]
5 : [9]
6 : [1, 2, 4, 8]
7 : [1, 4, 8]
8 : [2, 3, 4, 6, 7]
9 : [1, 2, 3, 5] 
```
The calc_similarity_scores function should create the following similarity matrix:
```
0 : [3, 0, 1, 1, 1, 0, 2, 1, 2, 3]
1 : [0, 5, 3, 2, 2, 1, 1, 1, 3, 0]
2 : [1, 3, 5, 3, 2, 1, 1, 1, 2, 1]
3 : [1, 2, 3, 4, 1, 1, 2, 1, 1, 1]
4 : [1, 2, 2, 1, 4, 0, 2, 2, 2, 1]
5 : [0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
6 : [2, 1, 1, 2, 2, 0, 4, 3, 2, 2]
7 : [1, 1, 1, 1, 2, 0, 3, 3, 1, 1]
8 : [2, 3, 2, 1, 2, 0, 2, 1, 5, 2]
9 : [3, 0, 1, 1, 1, 0, 2, 1, 2, 4] 
```
Test
```
Facebook friend recommendation.

Enter a filename: small_network_data.txt

Enter an integer in the range 0 to 9 : 0
The suggested friend for 0 is 9
Do you want to continue (enter y for yes)? y

Enter an integer in the range 0 to 9: 3
The suggested friend for 3 is 1
Do you want to continue (enter y for yes)? y

Enter an integer in the range 0 to 9: 8
The suggested friend for 8 is 1
Do you want to continue (enter y for yes)? No
```
