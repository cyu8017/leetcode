<?php
// LeetCode 0340 - Longest Substring with At Most K Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function lengthOfLongestSubstringKDistinct($s, $k) {
        return $this->length_of_longest_substring_k_distinct($s, $k);
    }

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function length_of_longest_substring_k_distinct($s, $k) {
        if ($k === 0) {
            return 0;
        }

        $counts = [];
        $left = 0;
        $best = 0;
        $length = strlen($s);

        for ($right = 0; $right < $length; $right++) {
            $char = $s[$right];
            if (!array_key_exists($char, $counts)) {
                $counts[$char] = 0;
            }
            $counts[$char]++;
            while (count($counts) > $k) {
                $leftChar = $s[$left];
                $counts[$leftChar]--;
                if ($counts[$leftChar] === 0) {
                    unset($counts[$leftChar]);
                }
                $left++;
            }
            $best = max($best, $right - $left + 1);
        }

        return $best;
    }
}
