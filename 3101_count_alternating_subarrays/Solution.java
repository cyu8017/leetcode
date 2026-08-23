// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

class Solution {
    public long countAlternatingSubarrays(int[] nums) {
        long ans = 1, s = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) s++;
            else s = 1;
            ans += s;
        }
        return ans;
    }
}
