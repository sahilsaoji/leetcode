##a number of bids are being taken for a project. Determine the number of distinct pairs of project costs where their absolute difference is some target value. Two pairs are distinct if they differ in at least one value.
##
##Example:
##projectCosts = [1,3,5] target = 2
##There are 2 pairs [1,3] [3,5] that have the target difference targets = 2, therefore a value of 2 is returned 
##
##Answer this problem in python


def count_pairs_with_difference(project_costs, target):
    # Using a set for efficient lookups
    costs_set = set(project_costs)
    count = 0

    # Iterating through the costs and checking if the complement (cost + target) exists in the set
    for cost in project_costs:
        if cost + target in costs_set:
            count += 1

    return count

# Example usage
project_costs = [1, 3, 5, 6, 8, 9]
target = 3
print(count_pairs_with_difference(project_costs, target))
