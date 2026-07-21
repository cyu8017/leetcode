// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

using System;
using System.Collections.Generic;

public class Solution {
    private int batchSize;
    private Dictionary<long, int> memo;

    public int MaxHappyGroups(int batchSize, int[] groups) {
        this.batchSize = batchSize;
        int[] count = new int[batchSize];
        foreach (int size in groups) count[size % batchSize]++;

        memo = new Dictionary<long, int>();
        int ans = Dfs(0, count);
        if (count[0] > 0) ans += count[0] - 1;
        return ans;
    }

    private int Dfs(int remainder, int[] count) {
        long key = Encode(remainder, count);
        if (memo.TryGetValue(key, out int cached)) return cached;

        int best = 0;
        for (int mod = 1; mod < batchSize; mod++) {
            if (count[mod] == 0) continue;
            count[mod]--;
            best = Math.Max(best, Dfs((remainder + mod) % batchSize, count));
            count[mod]++;
        }

        int result = remainder == 0 ? best + 1 : best;
        memo[key] = result;
        return result;
    }

    private long Encode(int remainder, int[] count) {
        long key = remainder;
        foreach (int value in count) key = key * 31 + value;
        return key;
    }
}
