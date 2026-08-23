// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

using System.Collections.Generic;

public class Solution {
    public int[] MinReverseOperations(int n, int p, int[] banned, int k) {
        var ban = new HashSet<int>(banned);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        ans[p] = 0;
        var q = new Queue<(int, int)>();
        q.Enqueue((p, 0));
        while (q.Count > 0) {
            var (i, d) = q.Dequeue();
            int lo = i - (k - 1);
            if (lo < 0) lo = 0;
            int hi = i;
            if (hi > n - k) hi = n - k;
            for (int L = lo; L <= hi; ++L) {
                int R = L + k - 1;
                int ni = L + R - i;
                if (ni < 0 || ni >= n || ban.Contains(ni) || ans[ni] != -1) continue;
                ans[ni] = d + 1;
                q.Enqueue((ni, d + 1));
            }
        }
        return ans;
    }
}
