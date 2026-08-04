// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

import java.util.*;

class Solution {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        int[] freqs = new int[words.length];
        for (int i = 0; i < words.length; i++) freqs[i] = f(words[i]);
        Arrays.sort(freqs);
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int fq = f(queries[i]);
            int lo = 0, hi = freqs.length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (freqs[mid] <= fq) lo = mid + 1; else hi = mid;
            }
            ans[i] = freqs.length - lo;
        }
        return ans;
    }
    private int f(String s) {
        char min = 'z';
        for (char c : s.toCharArray()) if (c < min) min = c;
        int cnt = 0;
        for (char c : s.toCharArray()) if (c == min) cnt++;
        return cnt;
    }
}
