// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        Deque<Integer> stack = new ArrayDeque<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (!stack.isEmpty() && stack.peekLast() > x && stack.size() - 1 + n - i >= k) {
                stack.removeLast();
            }
            if (stack.size() < k) {
                stack.addLast(x);
            }
        }
        int[] ans = new int[k];
        int i = 0;
        for (int v : stack) {
            ans[i++] = v;
        }
        return ans;
    }
}
