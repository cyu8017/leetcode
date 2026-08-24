<?php
// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution {
    /**
     * @param string $s
     * @return int
     */
    function findSubstringInWraproundString($s) {
        return $this->find_substring_in_wrapround_string($s);
    }

    /**
     * @param string $s
     * @return int
     */
    function find_substring_in_wrapround_string($s) {
        $counts = array_fill(0, 26, 0);
        $length = 0;
        $chars = str_split($s);

        foreach ($chars as $index => $char) {
            if ($index > 0 && (ord($char) - ord($chars[$index - 1]) + 26) % 26 === 1) {
                $length++;
            } else {
                $length = 1;
            }
            $position = ord($char) - ord('a');
            $counts[$position] = max($counts[$position], $length);
        }

        return array_sum($counts);
    }
}
