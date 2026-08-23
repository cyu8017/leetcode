// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

class Solution {
    public long shiftDistance(String s, String t, int[] nextCost, int[] previousCost) {
        long ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int a = s.charAt(i) - 'a', b = t.charAt(i) - 'a';
            if (a == b) continue;
            long fwd = 0;
            for (int x = a; x != b; x = (x + 1) % 26) fwd += nextCost[x];
            long bwd = 0;
            for (int x = a; x != b; x = (x + 25) % 26) bwd += previousCost[x];
            ans += fwd < bwd ? fwd : bwd;
        }
        return ans;
    }
}
