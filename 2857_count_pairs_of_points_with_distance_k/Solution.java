// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int countPairs(List<List<Integer>> coordinates, int k) {
        Map<Long, Integer> freq = new HashMap<>();
        int ans = 0;
        for (List<Integer> p : coordinates) {
            int x = p.get(0), y = p.get(1);
            for (int a = 0; a <= k; a++) {
                int b = k - a;
                ans += freq.getOrDefault(key(x ^ a, y ^ b), 0);
            }
            freq.merge(key(x, y), 1, Integer::sum);
        }
        return ans;
    }

    private long key(int x, int y) {
        return (((long) x) << 32) ^ (y & 0xffffffffL);
    }
}
