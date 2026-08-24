// CONFIG class=Solution method=maxPalindromicSubarraySum types=None
// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

class Solution {
    public long maxPalindromicSubarraySum(int[] nums) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        int[] odd = new int[n];
        int left = 0, right = -1;
        for (int i = 0; i < n; i++) {
            int radius = 1;
            if (i <= right) {
                int mirror = left + right - i;
                radius = odd[mirror];
                if (right - i + 1 < radius) radius = right - i + 1;
            }
            while (i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius]) radius++;
            odd[i] = radius;
            if (i + radius - 1 > right) {
                left = i - radius + 1;
                right = i + radius - 1;
            }
        }
        int[] even = new int[n];
        left = 0; right = -1;
        for (int i = 0; i < n; i++) {
            int radius = 0;
            if (i <= right) {
                int mirror = left + right - i + 1;
                radius = even[mirror];
                if (right - i + 1 < radius) radius = right - i + 1;
            }
            while (i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius]) radius++;
            even[i] = radius;
            if (i + radius - 1 > right) {
                left = i - radius;
                right = i + radius - 1;
            }
        }
        long answer = 0;
        for (int i = 0; i < n; i++) {
            long sum = prefix[i + odd[i]] - prefix[i - odd[i] + 1];
            if (sum > answer) answer = sum;
            if (even[i] > 0) {
                sum = prefix[i + even[i]] - prefix[i - even[i]];
                if (sum > answer) answer = sum;
            }
        }
        return answer;
    }
}
