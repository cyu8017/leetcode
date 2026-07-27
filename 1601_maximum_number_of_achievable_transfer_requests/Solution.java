// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution {
    public int maximumRequests(int n, int[][] requests) {
        int ans = 0;
        int m = requests.length;
        for (int mask = 0; mask < (1 << m); mask++) {
            int bits = Integer.bitCount(mask);
            if (bits <= ans) continue;
            int[] bal = new int[n];
            for (int i = 0; i < m; i++) {
                if (((mask >> i) & 1) == 1) {
                    bal[requests[i][0]]--;
                    bal[requests[i][1]]++;
                }
            }
            boolean ok = true;
            for (int b : bal) {
                if (b != 0) { ok = false; break; }
            }
            if (ok) ans = bits;
        }
        return ans;
    }
}
