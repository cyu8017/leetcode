// LeetCode 0340 - Longest Substring with At Most K Distinct Characters

// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/



using System.Collections.Generic;



public class Solution {

    public int LengthOfLongestSubstringKDistinct(string s, int k) {

        if (k == 0) {

            return 0;

        }



        Dictionary<char, int> counts = new();

        int left = 0;

        int best = 0;



        for (int right = 0; right < s.Length; right++) {

            char ch = s[right];

            counts[ch] = counts.GetValueOrDefault(ch) + 1;



            while (counts.Count > k) {

                char leftChar = s[left];

                counts[leftChar]--;

                if (counts[leftChar] == 0) {

                    counts.Remove(leftChar);

                }

                left++;

            }



            best = Math.Max(best, right - left + 1);

        }



        return best;

    }

}
