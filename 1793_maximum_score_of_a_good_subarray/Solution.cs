// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

public class Solution {
    public int MaximumScore(int[] nums, int k) {
        int n = nums.Length;
        var stack = new Stack<int>();
        long ans = 0;
        for (int i = 0; i <= n; i++) {
            while (stack.Count > 0 && (i == n || nums[i] < nums[stack.Peek()])) {
                int mid = stack.Pop();
                int left = stack.Count > 0 ? stack.Peek() + 1 : 0;
                int right = i - 1;
                if (left <= k && k <= right) {
                    ans = Math.Max(ans, (long)nums[mid] * (right - left + 1));
                }
            }
            stack.Push(i);
        }
        return (int)ans;
    }
}
