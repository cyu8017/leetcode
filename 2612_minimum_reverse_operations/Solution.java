// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int[] minReverseOperations(int n, int p, int[] banned, int k) {
        Set<Integer> ban = new HashSet<>();
        for (int b : banned) ban.add(b);
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        ans[p] = 0;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {p, 0});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int i = cur[0], d = cur[1];
            int lo = i - (k - 1);
            if (lo < 0) lo = 0;
            int hi = i;
            if (hi > n - k) hi = n - k;
            for (int L = lo; L <= hi; ++L) {
                int R = L + k - 1;
                int ni = L + R - i;
                if (ni < 0 || ni >= n || ban.contains(ni) || ans[ni] != -1) continue;
                ans[ni] = d + 1;
                q.offer(new int[] {ni, d + 1});
            }
        }
        return ans;
    }
}
