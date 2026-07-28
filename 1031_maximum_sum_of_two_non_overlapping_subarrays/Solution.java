// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        int[] prefix = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) prefix[i + 1] = prefix[i] + nums[i];
        return Math.max(best(prefix, firstLen, secondLen), best(prefix, secondLen, firstLen));
    }

    private int best(int[] prefix, int a, int b) {
        int bestA = 0, ans = 0;
        for (int i = a + b; i < prefix.length; i++) {
            bestA = Math.max(bestA, prefix[i - b] - prefix[i - b - a]);
            ans = Math.max(ans, bestA + prefix[i] - prefix[i - b]);
        }
        return ans;
    }
}
