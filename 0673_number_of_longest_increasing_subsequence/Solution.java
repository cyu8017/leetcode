// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        int[] lengths = new int[n];
        int[] counts = new int[n];
        for (int i = 0; i < n; ++i) {
            lengths[i] = 1;
            counts[i] = 1;
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] >= nums[i]) {
                    continue;
                }
                if (lengths[j] + 1 > lengths[i]) {
                    lengths[i] = lengths[j] + 1;
                    counts[i] = counts[j];
                } else if (lengths[j] + 1 == lengths[i]) {
                    counts[i] += counts[j];
                }
            }
        }
        int longest = 0;
        for (int length : lengths) {
            longest = Math.max(longest, length);
        }
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            if (lengths[i] == longest) {
                answer += counts[i];
            }
        }
        return answer;
    }
}
