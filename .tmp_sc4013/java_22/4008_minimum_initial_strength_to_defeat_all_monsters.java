// CONFIG class=Solution method=minInitialStrength types=None
// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

class Solution {
    public long minInitialStrength(int[] monsters, int[][] boosts) {
        int n = monsters.length;
        long[] d = new long[n + 1];
        for (int[] b : boosts) {
            d[b[0]] += b[2];
            d[b[1] + 1] -= b[2];
        }
        long left = 0, right = 1000000000000000L;
        while (left < right) {
            long mid = (left + right) / 2;
            if (check(mid, monsters, d)) right = mid;
            else left = mid + 1;
        }
        return left;
    }

    private boolean check(long v, int[] monsters, long[] d) {
        long bonus = 0;
        for (int i = 0; i < monsters.length; i++) {
            bonus += d[i];
            if (v + bonus < monsters[i]) return false;
            v -= monsters[i];
            if (v < 0) v = 0;
        }
        return true;
    }
}
