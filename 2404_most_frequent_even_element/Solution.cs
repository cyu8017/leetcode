// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

using System.Collections.Generic;

public class Solution {
    public int MostFrequentEven(int[] nums) {
        var cnt = new Dictionary<int, int>();
        int ans = -1, best = 0;
        foreach (int x in nums) {
            if (x % 2 != 0) continue;
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
            if (cnt[x] > best || (cnt[x] == best && (ans == -1 || x < ans))) {
                best = cnt[x];
                ans = x;
            }
        }
        return ans;
    }
}
