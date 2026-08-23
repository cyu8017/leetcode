// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

public class Solution {
    public int AtMostNGivenDigitSet(string[] digits, int n) {
        string s = n.ToString();
        int m = s.Length;
        int k = digits.Length;

        int Ipow(int bas, int exp) {
            int r = 1;
            while (exp-- > 0) r *= bas;
            return r;
        }

        int CountUpTo(string t) {
            if (t.Length == 0) return 0;
            int first = 0;
            foreach (var d in digits) if (d[0] < t[0]) first++;
            int ways = first * Ipow(k, t.Length - 1);
            bool found = false;
            foreach (var d in digits) {
                if (d[0] == t[0]) { found = true; break; }
            }
            if (found) ways += CountUpTo(t.Substring(1));
            return ways;
        }

        int ans = 0;
        for (int i = 1; i < m; i++) ans += Ipow(k, i);
        ans += CountUpTo(s);
        return ans;
    }
}
