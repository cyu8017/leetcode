// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

using System;

public class Solution {
    public int Score(string[] cards, char x) {
        int xx = 0;
        int[] left = new int[26], right = new int[26];
        foreach (var c in cards) {
            char a = c[0], b = c[1];
            if (a == x && b == x) xx++;
            else if (a == x) left[b - 'a']++;
            else if (b == x) right[a - 'a']++;
        }
        (int pairs, int rem) PairGroup(int[] arr) {
            int total = 0, mx = 0;
            for (int i = 0; i < 26; i++) {
                total += arr[i];
                mx = Math.Max(mx, arr[i]);
            }
            int pairs = total / 2;
            if (total - mx < pairs) pairs = total - mx;
            return (pairs, total - 2 * pairs);
        }
        var (lp, lr) = PairGroup(left);
        var (rp, rr) = PairGroup(right);
        int ans = lp + rp;
        int rem = lr + rr;
        int use = Math.Min(xx, rem);
        ans += use;
        xx -= use;
        ans += xx / 2;
        return ans;
    }
}
