// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int maxSumMinProduct(int[] nums) {
        int mod = 1_000_000_007;
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        int[] leftBound = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peekLast()] >= nums[i]) {
                stack.removeLast();
            }
            leftBound[i] = stack.isEmpty() ? -1 : stack.peekLast();
            stack.addLast(i);
        }

        int[] rightBound = new int[n];
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peekLast()] >= nums[i]) {
                stack.removeLast();
            }
            rightBound[i] = stack.isEmpty() ? n : stack.peekLast();
            stack.addLast(i);
        }

        long best = 0;
        for (int i = 0; i < n; i++) {
            long total = prefix[rightBound[i]] - prefix[leftBound[i] + 1];
            best = Math.max(best, total * nums[i]);
        }

        return (int) (best % mod);
    }
}
