// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int maxResult(int[] nums, int k) {
        Deque<int[]> q = new ArrayDeque<>();
        q.addLast(new int[] {0, nums[0]});
        for (int i = 1; i < nums.length; i++) {
            while (q.peekFirst()[0] < i - k) {
                q.removeFirst();
            }
            int score = nums[i] + q.peekFirst()[1];
            while (!q.isEmpty() && q.peekLast()[1] <= score) {
                q.removeLast();
            }
            q.addLast(new int[] {i, score});
        }
        return q.peekLast()[1];
    }
}
