// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

class Solution {
    public int[] countOppositeParity(int[] nums) {
        int[] cnt = { 0, 0 };
        for (int x : nums) cnt[x & 1]++;
        int n = nums.length;
        var ans = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            cnt[x & 1]--;
            ans[i] = cnt[(x & 1) ^ 1];
        }
        return ans;
    }
}
