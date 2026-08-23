// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

using System;
using System.Linq;

public class Solution {
    public string OrderlyQueue(string s, int k) {
        if (k > 1) {
            var chars = s.ToCharArray();
            Array.Sort(chars);
            return new string(chars);
        }
        string best = s;
        for (int i = 1; i < s.Length; i++) {
            string cand = s.Substring(i) + s.Substring(0, i);
            if (string.CompareOrdinal(cand, best) < 0) best = cand;
        }
        return best;
    }
}
