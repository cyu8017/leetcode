// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

using System;
using System.Numerics;

public class Solution {
    public int MaximumRequests(int n, int[][] requests) {
        int ans = 0, m = requests.Length;
        for (int mask = 0; mask < (1 << m); mask++) {
            int bits = BitOperations.PopCount((uint)mask);
            if (bits <= ans) continue;
            var bal = new int[n];
            for (int i = 0; i < m; i++) {
                if (((mask >> i) & 1) == 0) continue;
                bal[requests[i][0]]--;
                bal[requests[i][1]]++;
            }
            bool ok = true;
            foreach (int b in bal) if (b != 0) { ok = false; break; }
            if (ok) ans = bits;
        }
        return ans;
    }
}
