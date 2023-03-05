# Jump Game IV
 
 Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Returnthe minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108


# Explanation

The Jump Game IV problem is a graph traversal problem that requires you to find the minimum number of steps to reach the end of an array of integers starting from the first index. The array represents a graph where each element is a node, and the value of the element represents the number of steps you can take from that node.

For example, given the array [4,2,3,0,3,1,2], you can start at index 0 and take 4 steps to reach index 4, which has a value of 3. From there, you can take 3 steps to reach index 3, which has a value of 0, and so on until you reach the last index.

To solve this problem, you can use a Breadth-First Search (BFS) approach, where you start from the first index and traverse the graph level by level until you reach the end. You can keep track of the number of steps taken to reach each node and use a set to avoid revisiting the same node.

Here's a high-level overview of the algorithm:

1. Create a queue and add the first index to it.
2. Create a set to keep track of visited nodes and add the first index to it.
3. Create a dictionary to store the number of steps taken to reach each node and initialize it with the first index and a value of 0.
4. While the queue is not empty:
  - Dequeue the next index from the queue.
  - If the dequeued index is the last index, return the number of steps taken to reach it.
  - For each neighbor of the dequeued index:
    
    1- If the neighbor is not visited:
     - Add it to the queue.
     - Add it to the visited set.
     - Add its number of steps to the dictionary with a value of the number of steps taken to reach the dequeued index plus one.
If the last index is not reached, return -1.
