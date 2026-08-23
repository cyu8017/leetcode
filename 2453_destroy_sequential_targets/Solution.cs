// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

using System.Collections.Generic;

public class Solution {
    public int DestroyTargets(int[] nums, int space) {
        var cnt = new Dictionary<int, int>();
        foreach (int x in nums) {
            int m = x % space;
            if (!cnt.ContainsKey(m)) cnt[m] = 0;
            cnt[m]++;
        }
        int bestCnt = 0;
        foreach (int c in cnt.Values) if (c > bestCnt) bestCnt = c;
        int ans = 1000000000;
        foreach (var kv in cnt) {
            if (kv.Value == bestCnt) {
                foreach (int x in nums) {
                    if (x % space == kv.Key && x < ans) ans = x;
                }
            }
        }
        return ans;
    }
}
