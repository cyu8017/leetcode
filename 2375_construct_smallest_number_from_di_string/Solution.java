// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution {
    public String smallestNumber(String pattern) {
        int n = pattern.length();
        char[] ans = new char[n + 1];
        for (int i = 0; i <= n; i++) ans[i] = (char) ('1' + i);
        int i = 0;
        while (i < n) {
            if (pattern.charAt(i) == 'I') {
                i++;
                continue;
            }
            int j = i;
            while (j < n && pattern.charAt(j) == 'D') j++;
            reverse(ans, i, j);
            i = j;
        }
        return new String(ans);
    }

    private void reverse(char[] a, int l, int r) {
        while (l < r) {
            char t = a[l];
            a[l] = a[r];
            a[r] = t;
            l++;
            r--;
        }
    }
}
