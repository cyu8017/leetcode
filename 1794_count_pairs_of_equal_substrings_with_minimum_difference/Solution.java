// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

import java.util.Arrays;

class Solution {
    public long countQuadruples(String firstString, String secondString) {
        int[] first = new int[26];
        int[] lastF = new int[26];
        int[] lastS = new int[26];
        Arrays.fill(first, -1);
        Arrays.fill(lastF, -1);
        Arrays.fill(lastS, -1);
        for (int i = 0; i < firstString.length(); i++) {
            int c = firstString.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            lastF[c] = i;
        }
        for (int i = 0; i < secondString.length(); i++) {
            lastS[secondString.charAt(i) - 'a'] = i;
        }
        long best = Long.MAX_VALUE;
        for (int c = 0; c < 26; c++) {
            if (first[c] != -1 && lastS[c] != -1) {
                best = Math.min(best, (long) lastF[c] - lastS[c]);
            }
        }
        if (best == Long.MAX_VALUE) return 0;
        long ans = 0;
        for (int c = 0; c < 26; c++) {
            if (first[c] == -1 || lastS[c] == -1 || lastF[c] - lastS[c] != best) continue;
            long iCount = 0;
            for (int k = first[c]; k <= lastF[c]; k++) {
                if (firstString.charAt(k) - 'a' == c) iCount++;
            }
            long aCount = 0;
            for (int k = 0; k <= lastS[c]; k++) {
                if (secondString.charAt(k) - 'a' == c) aCount++;
            }
            ans += iCount * aCount;
        }
        return ans;
    }
}
