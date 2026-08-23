// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

using System.Collections.Generic;

public class Solution {
    public int AlternatingXOR(int[] nums, int target1, int target2) {
        const int MOD = 1000000007;
        var cnt1 = new Dictionary<int, int>();
        var cnt2 = new Dictionary<int, int> { [0] = 1 };
        int pre = 0, ans = 0;
        foreach (int x in nums) {
            pre ^= x;
            int a = cnt2.ContainsKey(pre ^ target1) ? cnt2[pre ^ target1] : 0;
            int b = cnt1.ContainsKey(pre ^ target2) ? cnt1[pre ^ target2] : 0;
            ans = (a + b) % MOD;
            if (!cnt1.ContainsKey(pre)) cnt1[pre] = 0;
            if (!cnt2.ContainsKey(pre)) cnt2[pre] = 0;
            cnt1[pre] = (cnt1[pre] + a) % MOD;
            cnt2[pre] = (cnt2[pre] + b) % MOD;
        }
        return ans;
    }
}
