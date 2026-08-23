// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

using System.Collections.Generic;

public class Solution {
    public int MakePrefSumNonNegative(int[] nums) {
        var h = new PriorityQueue<int, int>();
        long sum = 0;
        int ans = 0;
        foreach (int x in nums) {
            sum += x;
            if (x < 0) h.Enqueue(x, x);
            if (sum < 0) {
                int worst = h.Dequeue();
                sum -= worst;
                ans++;
            }
        }
        return ans;
    }
}
