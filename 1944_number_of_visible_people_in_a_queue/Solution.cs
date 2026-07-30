// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

using System.Collections.Generic;

public class Solution {
    public int[] CanSeePersonsCount(int[] heights) {
        int n = heights.Length;
        var ans = new int[n];
        var stack = new Stack<int>();
        for (int i = n - 1; i >= 0; i--) {
            int count = 0;
            while (stack.Count > 0 && heights[i] > stack.Peek()) {
                stack.Pop();
                count++;
            }
            if (stack.Count > 0) count++;
            ans[i] = count;
            stack.Push(heights[i]);
        }
        return ans;
    }
}