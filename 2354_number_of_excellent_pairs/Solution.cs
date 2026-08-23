// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

using System.Collections.Generic;

public class Solution {
    public long CountExcellentPairs(int[] nums, int k) {
        var uniq = new HashSet<int>(nums);
        int[] cnt = new int[32];
        foreach (int x in uniq) {
            int bits = 0;
            for (int y = x; y > 0; y >>= 1) bits += y & 1;
            cnt[bits]++;
        }
        long ans = 0;
        for (int i = 0; i < 32; i++)
            for (int j = 0; j < 32; j++)
                if (i + j >= k) ans += (long)cnt[i] * cnt[j];
        return ans;
    }
}
