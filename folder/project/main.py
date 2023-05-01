# NAME: <Daniel Gao>
# DATE: 2023-04-14
# DESCRIPTION: Assignment 13, social network program to practice with Lists, Nested lists, Dictionaries, Functions

from typing import IO, List, Dict


def open_file() -> IO:
    """
    prompts user to enter file name and tries to open file.
    returns the file
    """
    while True:
        try:
            file_name = input("Enter file name: ")
            file = open(file_name, "r")
            return file
        except FileNotFoundError:
            print("Error in filename.")


def create_network(fp: IO) -> Dict[int, List[int]]:
    """
    creates dictionary that corresponds each user id to a list
    consisting of its friends' ids.
    returns dictionary
    """
    size = int(fp.readline())
    network = {}
    for i in range(size):
        network[i] = []

    # read friend info from file
    for line in fp:
        id_list = line.split()
        id1 = int(id_list[0])
        id2 = int(id_list[1])
        network[id1].append(id2)
        network[id2].append(id1)

    return network


def init_matrix(size: int) -> List[List[int]]:
    """
    creates n x n matrix initialized with zeroes
    returns matrix as nested list of lists
    """
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(0)

    return matrix


def common_degree(list1: List, list2: List) -> int:
    """
    calculates degree (common friends) between two lists
    returns degree
    """
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1

    return count


def calc_similarity_scores(network: Dict[int, List[int]]) -> List[List[int]]:
    """
    calculates the similarity matrix for all users in network
    returns similarity matrix
    """
    # initialize matrix
    similarity_matrix = init_matrix(len(network))
    for i in range(len(network)):
        for j in range(i, len(network)):
            # calculate common degree between user i and j
            degree = common_degree(network[i], network[j])
            # set similarity scores
            similarity_matrix[i][j] = degree
            similarity_matrix[j][i] = degree

    return similarity_matrix


def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    """
    recommends a friend for given member_id based on friend_list and similarity_list
    """
    max_sim = max(similarity_list)
    # iterate over similarity values in descending order
    while max_sim >= 0:
        for i in range(len(similarity_list)):
            if similarity_list[i] == max_sim and i not in friend_list and i != member_id:
                return i
        max_sim -= 1

    # if no recommended friend is found
    return -1


def main():
    print("Facebook friend recommendation.")

    network = create_network(open_file())
    similarity_matrix = calc_similarity_scores(network)

    n = len(network) - 1
    response = "Y"
    while response.upper() == "Y":
        member_id = input(f"Enter an integer in the range 0 to {n}: ")
        if not member_id.isdigit() or not (0 <= int(member_id) <= n):
            print(f"Error: input must be an int between 0 and {n}")
        else:
            member_id = int(member_id)
            suggested_friend_id = recommend(member_id, network[member_id], similarity_matrix[member_id])
            print(f"The suggested friend for {member_id} is {suggested_friend_id}")
            response = input("Do you want to continue (enter y for yes)?").strip().lower()


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()