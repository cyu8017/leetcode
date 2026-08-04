// LeetCode 1395 - Count Number Of Teams
// https://leetcode.com/problems/count-number-of-teams/

class Solution {
    public int numTeams(int[] rating) {
        int ans = 0, n = rating.length;
        for (int j = 0; j < n; j++) {
            int x = rating[j], ll = 0, lg = 0, rl = 0, rg = 0;
            for (int i = 0; i < j; i++) if (rating[i] < x) ll++; else lg++;
            for (int i = j + 1; i < n; i++) if (rating[i] > x) rg++; else rl++;
            ans += ll * rg + lg * rl;
        }
        return ans;
    }
}
