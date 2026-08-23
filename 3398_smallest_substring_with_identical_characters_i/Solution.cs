// LeetCode 3398 - Smallest Substring With Identical Characters I
// https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

public class Solution {
    public int MinLength(string s, int numOps) {
        int n = s.Length;
        bool Ok(int L) {
            if (L == 0) return false;
            int ops = 0;
            for (int i = 0; i < n; ) {
                int j = i;
                while (j < n && s[j] == s[i]) j++;
                ops += (j - i) / (L + 1);
                i = j;
            }
            return ops <= numOps;
        }
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
