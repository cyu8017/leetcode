// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

class Solution {
    private long calc(String s, String t) {
        long cnt = 0, a = 0;
        for (char c : s.toCharArray()) {
            if (c == t.charAt(1)) cnt += a;
            if (c == t.charAt(0)) a++;
        }
        return cnt;
    }

    public long numOfSubsequences(String s) {
        long l = 0, r = 0;
        for (char c : s.toCharArray())
            if (c == 'T') r++;
        long ans = 0, mx = 0;
        for (char c : s.toCharArray()) {
            if (c == 'T') r--;
            if (c == 'C') ans += l * r;
            if (c == 'L') l++;
            mx = Math.max(mx, l * r);
        }
        mx = Math.max(mx, Math.max(calc(s, "LC"), calc(s, "CT")));
        return ans + mx;
    }
}
