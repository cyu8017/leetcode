<?php
// LeetCode 0395 - Longest Substring with At Least K Repeating Characters
// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function longestSubstring($s, $k) {
        return $this->longest_substring($s, $k);
    }

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function longest_substring($s, $k) {
        if ($s === "") {
            return 0;
        }

        $counts = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $char = $s[$index];
            if (!isset($counts[$char])) {
                $counts[$char] = 0;
            }
            $counts[$char]++;
        }

        foreach ($counts as $char => $count) {
            if ($count < $k) {
                $parts = explode($char, $s);
                $best = 0;
                foreach ($parts as $part) {
                    $best = max($best, $this->longest_substring($part, $k));
                }
                return $best;
            }
        }

        return $length;
    }
}
