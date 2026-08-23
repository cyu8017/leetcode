// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

public class Solution {
    public int CountSubranges(int[] nums1, int[] nums2) {
        const int MOD = 1000000007;
        int n = nums1.Length, ans = 0;
        var dp = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            var ndp = new Dictionary<int, int>();
            ndp[nums1[i]] = (ndp.GetValueOrDefault(nums1[i]) + 1) % MOD;
            ndp[-nums2[i]] = (ndp.GetValueOrDefault(-nums2[i]) + 1) % MOD;
            foreach (var kv in dp) {
                int diff = kv.Key, cnt = kv.Value;
                ndp[diff + nums1[i]] = (ndp.GetValueOrDefault(diff + nums1[i]) + cnt) % MOD;
                ndp[diff - nums2[i]] = (ndp.GetValueOrDefault(diff - nums2[i]) + cnt) % MOD;
            }
            dp = ndp;
            ans = (ans + dp.GetValueOrDefault(0)) % MOD;
        }
        return ans;
    }
}
