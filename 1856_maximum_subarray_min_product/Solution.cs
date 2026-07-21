// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

public class Solution {
    public int MaxSumMinProduct(int[] nums) {
        const int mod = 1_000_000_007;
        int n = nums.Length;
        var prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        var leftBound = new int[n];
        var stack = new List<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack[^1]] >= nums[i]) {
                stack.RemoveAt(stack.Count - 1);
            }
            leftBound[i] = stack.Count == 0 ? -1 : stack[^1];
            stack.Add(i);
        }

        var rightBound = new int[n];
        stack.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack[^1]] >= nums[i]) {
                stack.RemoveAt(stack.Count - 1);
            }
            rightBound[i] = stack.Count == 0 ? n : stack[^1];
            stack.Add(i);
        }

        long best = 0;
        for (int i = 0; i < n; i++) {
            long total = prefix[rightBound[i]] - prefix[leftBound[i] + 1];
            best = Math.Max(best, total * nums[i]);
        }
        return (int)(best % mod);
    }
}
