// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

public class Solution {
    public int MaxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        var prefix = new int[nums.Length + 1];
        for (int i = 0; i < nums.Length; i++) prefix[i + 1] = prefix[i] + nums[i];
        return Math.Max(Best(prefix, firstLen, secondLen), Best(prefix, secondLen, firstLen));
    }

    private static int Best(int[] prefix, int a, int b) {
        int bestA = 0, ans = 0;
        for (int i = a + b; i < prefix.Length; i++) {
            bestA = Math.Max(bestA, prefix[i - b] - prefix[i - b - a]);
            ans = Math.Max(ans, bestA + prefix[i] - prefix[i - b]);
        }
        return ans;
    }
}
