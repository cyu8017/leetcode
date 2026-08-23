// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));
        int[][] qs = new int[queries.length][2];
        for (int i = 0; i < queries.length; i++) {
            qs[i][0] = queries[i];
            qs[i][1] = i;
        }
        Arrays.sort(qs, (a, b) -> Integer.compare(a[0], b[0]));
        int[] ans = new int[queries.length];
        Map<Integer, Integer> cnt = new HashMap<>();
        int active = 0, l = 0, r = 0;
        for (int[] q : qs) {
            int t = q[0], qi = q[1];
            while (r < logs.length && logs[r][1] <= t) {
                int id = logs[r][0];
                int c = cnt.getOrDefault(id, 0);
                if (c == 0) active++;
                cnt.put(id, c + 1);
                r++;
            }
            while (l < r && logs[l][1] < t - x) {
                int id = logs[l][0];
                int c = cnt.get(id) - 1;
                cnt.put(id, c);
                if (c == 0) active--;
                l++;
            }
            ans[qi] = n - active;
        }
        return ans;
    }
}
