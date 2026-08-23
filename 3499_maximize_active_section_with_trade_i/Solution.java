// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        int ones = 0;
        for (char c : s.toCharArray()) if (c == '1') ones++;
        List<int[]> zeros = new ArrayList<>();
        int n = s.length();
        for (int i = 0; i < n; ) {
            if (s.charAt(i) != '0') { i++; continue; }
            int j = i;
            while (j < n && s.charAt(j) == '0') j++;
            zeros.add(new int[]{i, j - 1});
            i = j;
        }
        int best = 0;
        for (int i = 0; i + 1 < zeros.size(); i++) {
            int gain = (zeros.get(i)[1] - zeros.get(i)[0] + 1) + (zeros.get(i + 1)[1] - zeros.get(i + 1)[0] + 1);
            if (gain > best) best = gain;
        }
        return ones + best;
    }
}
