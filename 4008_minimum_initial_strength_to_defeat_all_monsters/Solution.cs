// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

public class Solution {
    public long MinInitialStrength(int[] monsters, int[][] boosts) {
        int n = monsters.Length;
        long[] d = new long[n + 1];
        foreach (var b in boosts) {
            d[b[0]] += b[2];
            d[b[1] + 1] -= b[2];
        }
        bool Check(long v) {
            long bonus = 0;
            for (int i = 0; i < n; i++) {
                bonus += d[i];
                if (v + bonus < monsters[i]) return false;
                v -= monsters[i];
                if (v < 0) v = 0;
            }
            return true;
        }
        long left = 0, right = 1000000000000000L;
        while (left < right) {
            long mid = (left + right) / 2;
            if (Check(mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }
}
