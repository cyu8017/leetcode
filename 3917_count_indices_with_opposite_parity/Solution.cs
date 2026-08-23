// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

public class Solution {
    public int[] CountOppositeParity(int[] nums) {
        int[] cnt = { 0, 0 };
        foreach (int x in nums) cnt[x & 1]++;
        int n = nums.Length;
        var ans = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            cnt[x & 1]--;
            ans[i] = cnt[(x & 1) ^ 1];
        }
        return ans;
    }
}
