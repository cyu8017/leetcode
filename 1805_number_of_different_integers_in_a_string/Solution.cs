// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

using System.Collections.Generic;

public class Solution {
    public int NumDifferentIntegers(string word) {
        var seen = new HashSet<string>();
        int i = 0, n = word.Length;
        while (i < n) {
            if (!char.IsDigit(word[i])) {
                i++;
                continue;
            }
            int j = i;
            while (j < n && char.IsDigit(word[j])) j++;
            string num = word.Substring(i, j - i).TrimStart('0');
            if (num.Length == 0) num = "0";
            seen.Add(num);
            i = j;
        }
        return seen.Count;
    }
}
