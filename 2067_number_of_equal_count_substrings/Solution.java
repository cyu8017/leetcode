// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

class Solution {
    public int equalCountSubstrings(String s, int count) {
        int ans = 0, n = s.length();
        boolean[] seen = new boolean[26];
        int maxUnique = 0;
        for (char c : s.toCharArray()) {
            if (!seen[c - 'a']) { seen[c - 'a'] = true; maxUnique++; }
        }
        for (int u = 1; u <= maxUnique; u++) {
            int needLen = u * count;
            if (needLen > n) break;
            int[] freq = new int[26];
            int have = 0;
            for (int i = 0; i < n; i++) {
                int c = s.charAt(i) - 'a';
                freq[c]++;
                if (freq[c] == count) have++;
                else if (freq[c] == count + 1) have--;
                if (i >= needLen) {
                    int p = s.charAt(i - needLen) - 'a';
                    if (freq[p] == count) have--;
                    else if (freq[p] == count + 1) have++;
                    freq[p]--;
                }
                if (i + 1 >= needLen && have == u) ans++;
            }
        }
        return ans;
    }
}
