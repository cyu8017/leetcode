// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

public class Solution {
    public long CountQuadruples(string firstString, string secondString) {
        var first = new int[26];
        var lastF = new int[26];
        var lastS = new int[26];
        Array.Fill(first, -1);
        Array.Fill(lastF, -1);
        Array.Fill(lastS, -1);
        for (int i = 0; i < firstString.Length; i++) {
            int c = firstString[i] - 'a';
            if (first[c] == -1) first[c] = i;
            lastF[c] = i;
        }
        for (int i = 0; i < secondString.Length; i++) {
            lastS[secondString[i] - 'a'] = i;
        }
        long best = long.MaxValue;
        for (int c = 0; c < 26; c++) {
            if (first[c] != -1 && lastS[c] != -1) {
                best = Math.Min(best, (long)lastF[c] - lastS[c]);
            }
        }
        if (best == long.MaxValue) return 0;
        long ans = 0;
        for (int c = 0; c < 26; c++) {
            if (first[c] == -1 || lastS[c] == -1 || lastF[c] - lastS[c] != best) continue;
            long iCount = 0;
            for (int k = first[c]; k <= lastF[c]; k++) {
                if (firstString[k] - 'a' == c) iCount++;
            }
            long aCount = 0;
            for (int k = 0; k <= lastS[c]; k++) {
                if (secondString[k] - 'a' == c) aCount++;
            }
            ans += iCount * aCount;
        }
        return ans;
    }
}
