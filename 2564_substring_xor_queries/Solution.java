// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[][] substringXorQueries(String s, int[][] queries) {
        Map<Integer, int[]> pos = new HashMap<>();
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            if (s.charAt(i) == '0') {
                pos.putIfAbsent(0, new int[] {i, i});
                continue;
            }
            int val = 0;
            for (int j = i; j < n && j < i + 30; ++j) {
                val = val * 2 + (s.charAt(j) - '0');
                pos.putIfAbsent(val, new int[] {i, j});
            }
        }
        int[][] ans = new int[queries.length][];
        for (int i = 0; i < queries.length; ++i) {
            int need = queries[i][0] ^ queries[i][1];
            ans[i] = pos.getOrDefault(need, new int[] {-1, -1}).clone();
        }
        return ans;
    }
}
