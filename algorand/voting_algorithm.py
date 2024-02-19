"""
The problem can be solved using the Boyer-Moore Voting Algorithm.
The algorithm is based on the fact that the majority element will always be the last element left after the elements
are paired up and removed.

The algorithm works as follows:
1. Initialize a variable, candidate, to store the majority element.
2. Initialize a variable, count, to store the count of the majority element.
3. Iterate through the array and for each element:
    a. If the count is 0, set the candidate to the current element and increment the count.
    b. If the current element is equal to the candidate, increment the count.
    c. If the current element is not equal to the candidate, decrement the count.
4. After the iteration, the candidate will be the majority element.
5. Iterate through the array again to count the occurrences of the candidate.
6. If the count of the candidate is greater than n/2, return the candidate as the majority element. Otherwise, indicate that no majority element exists.

The time complexity of the algorithm is O(n) and the space complexity is O(1).

The algorithm can be implemented in Python below:
"""

from __future__ import annotations


def find_majority_element(arr: list[int]) -> int | str:
    candidate = None
    count = 0
    n = len(arr)

    # Find the candidate
    for num in arr:
        if count == 0:
            candidate = num
            count += 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Count the occurrences of the candidate
    count_candidate = 0
    for num in arr:
        if num == candidate:
            count_candidate += 1

    # Check if the candidate is the majority element
    if count_candidate > n / 2:
        return candidate
    else:
        return "No majority element"
