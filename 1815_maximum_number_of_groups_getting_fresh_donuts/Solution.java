// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int batchSize;
    private Map<Long, Integer> memo;

    public int maxHappyGroups(int batchSize, int[] groups) {
        this.batchSize = batchSize;
        int[] count = new int[batchSize];
        for (int size : groups) {
            count[size % batchSize]++;
        }

        memo = new HashMap<>();
        int ans = dfs(0, count);
        if (count[0] > 0) {
            ans += count[0] - 1;
        }
        return ans;
    }

    private int dfs(int remainder, int[] count) {
        long key = encode(remainder, count);
        Integer cached = memo.get(key);
        if (cached != null) {
            return cached;
        }

        int best = 0;
        for (int mod = 1; mod < batchSize; mod++) {
            if (count[mod] == 0) {
                continue;
            }
            count[mod]--;
            best = Math.max(best, dfs((remainder + mod) % batchSize, count));
            count[mod]++;
        }

        int result = remainder == 0 ? best + 1 : best;
        memo.put(key, result);
        return result;
    }

    private long encode(int remainder, int[] count) {
        long key = remainder;
        for (int value : count) {
            key = key * 31 + value;
        }
        return key;
    }
}
