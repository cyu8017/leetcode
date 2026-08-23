// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

import java.util.Arrays;

class Solution {
    public boolean checkDistances(String s, int[] distance) {
        int[] first = new int[26];
        Arrays.fill(first, -1);
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            else if (i - first[c] - 1 != distance[c]) return false;
        }
        return true;
    }
}
