// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

public class Solution {
    public long MinTime(int[] skill, int[] mana) {
        int n = skill.Length, m = mana.Length;
        long[] done = new long[n];
        for (int j = 0; j < m; j++) {
            long t = 0;
            for (int i = 0; i < n; i++) {
                if (done[i] > t) t = done[i];
                t += (long)skill[i] * mana[j];
                done[i] = t;
            }
            for (int i = n - 2; i >= 0; i--)
                done[i] = done[i + 1] - (long)skill[i + 1] * mana[j];
        }
        return done[n - 1];
    }
}
