// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

public class Solution {
    public int MinTime(string s, int[] order, int k) {
        int n = s.Length;
        long total = 1L * n * (n + 1) / 2;
        if (k > total) return -1;
        long CountValid(int t) {
            bool[] star = new bool[n];
            for (int i = 0; i <= t; i++) star[order[i]] = true;
            long invalid = 0;
            for (int i = 0; i < n;) {
                if (star[i]) { i++; continue; }
                int j = i;
                while (j < n && !star[j]) j++;
                long L = j - i;
                invalid += L * (L + 1) / 2;
                i = j;
            }
            return total - invalid;
        }
        int lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (CountValid(mid) >= k) { ans = mid; hi = mid - 1; }
            else lo = mid + 1;
        }
        return ans;
    }
}
