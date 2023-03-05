from collections import deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:  # If there is only one element, no jumps are needed
            return 0

        # Create a dictionary to store the indices of each value in the array
        index_dict = {}
        for i, val in enumerate(arr):
            if val not in index_dict:
                index_dict[val] = set()
            index_dict[val].add(i)

        # Initialize the BFS queue and visited set
        queue = deque([0])
        visited = set([0])
        steps = {0: 0}  # Keep track of the number of steps taken to reach each index

        # BFS traversal of the array
        while queue:
            curr_index = queue.popleft()
            curr_steps = steps[curr_index]

            # Check if the end index has been reached
            if curr_index == n - 1:
                return curr_steps

            # Check neighbors of the current index
            for next_index in [curr_index - 1, curr_index + 1]:
                if next_index in visited or next_index < 0 or next_index >= n:
                    continue  # Skip already visited or out-of-bounds indices
                queue.append(next_index)
                visited.add(next_index)
                steps[next_index] = curr_steps + 1
            if arr[curr_index] in index_dict:
                for next_index in index_dict[arr[curr_index]]:
                    if next_index in visited or next_index == curr_index:
                        continue  # Skip already visited or same index
                    queue.append(next_index)
                    visited.add(next_index)
                    steps[next_index] = curr_steps + 1
                del index_dict[arr[curr_index]]  # Remove the set to save memory

        return -1  # End index could not be reached

sol = Solution()
print(sol.minJumps([7,6,9,6,9,6,9,7]))
print(sol.minJumps([100,-23,-23,404,100,23,23,23,3,404]))

