// LeetCode 0395 - Longest Substring with At Least K Repeating Characters

// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/



using System.Collections.Generic;

using System.Linq;



public class Solution {

    public int LongestSubstring(string s, int k) {

        if (string.IsNullOrEmpty(s)) {

            return 0;

        }



        Dictionary<char, int> counts = new();

        foreach (char character in s) {

            counts[character] = counts.GetValueOrDefault(character) + 1;

        }



        foreach (KeyValuePair<char, int> entry in counts) {

            if (entry.Value < k) {

                return s.Split(entry.Key).Max(part => LongestSubstring(part, k));

            }

        }



        return s.Length;

    }

}
