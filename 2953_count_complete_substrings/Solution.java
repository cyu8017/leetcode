// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

class Solution {
    public int countCompleteSubstrings(String word, int k) {
        int n = word.length(), ans = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j + 1 < n && Math.abs(word.charAt(j + 1) - word.charAt(j)) <= 2) j++;
            String seg = word.substring(i, j + 1);
            int m = seg.length();
            for (int chars = 1; chars <= 26; chars++) {
                int length = chars * k;
                if (length > m) break;
                int[] freq = new int[26];
                int unique = 0;
                for (int r = 0; r < m; r++) {
                    int c = seg.charAt(r) - 'a';
                    freq[c]++;
                    if (freq[c] == 1) unique++;
                    if (r >= length) {
                        int c2 = seg.charAt(r - length) - 'a';
                        freq[c2]--;
                        if (freq[c2] == 0) unique--;
                    }
                    if (r >= length - 1 && unique == chars) {
                        boolean ok = true;
                        for (int f : freq)
                            if (f != 0 && f != k) { ok = false; break; }
                        if (ok) ans++;
                    }
                }
            }
            i = j + 1;
        }
        return ans;
    }
}
