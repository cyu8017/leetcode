// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

using System;

public class Solution {
    public bool CheckDistances(string s, int[] distance) {
        int[] first = new int[26];
        Array.Fill(first, -1);
        for (int i = 0; i < s.Length; i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            else if (i - first[c] - 1 != distance[c]) return false;
        }
        return true;
    }
}
