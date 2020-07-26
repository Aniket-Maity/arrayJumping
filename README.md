Problem Statement
You are given an array of integers where each element represents the max number of jump that can be made forward from that element. Your task is to find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you can not jump at all which essentially means that you cannot move through that element.

Input Format
First line of the input will have an integer N representing the length of the array

Second line will have N number of space separated integers representing the maximum number of jumps allowed. 

Output Format
Integer representing number of minimum jumps required to cross through the array from the very first element, or -1 if crossing through the array is not possible

Constraints
Length of the array would be lesser than 1000

Each Array element would be lesser than 100

Time Limit
2s.
Each test case should pass in 2s.
Sample Input
11 
1 3 5 8 9 2 6 7 6 8 9
Sample Output
3