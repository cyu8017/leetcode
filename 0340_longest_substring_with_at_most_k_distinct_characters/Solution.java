// LeetCode 0340 - Longest Substring with At Most K Distinct Characters

// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/



import java.util.HashMap;

import java.util.Map;



class Solution {

    public int lengthOfLongestSubstringKDistinct(String s, int k) {

        if (k == 0) {

            return 0;

        }



        Map<Character, Integer> counts = new HashMap<>();

        int left = 0;

        int best = 0;



        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);

            counts.put(ch, counts.getOrDefault(ch, 0) + 1);



            while (counts.size() > k) {

                char leftChar = s.charAt(left);

                int nextCount = counts.get(leftChar) - 1;

                if (nextCount == 0) {

                    counts.remove(leftChar);

                } else {

                    counts.put(leftChar, nextCount);

                }

                left++;

            }



            best = Math.max(best, right - left + 1);

        }



        return best;

    }

}
