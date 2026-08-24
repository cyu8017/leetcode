<?php
// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution {
    /**
     * @param string $s
     * @param string $p
     * @return int[]
     */
    function findAnagrams($s, $p) {
        return $this->find_anagrams($s, $p);
    }

    /**
     * @param string $s
     * @param string $p
     * @return int[]
     */
    function find_anagrams($s, $p) {
        if (strlen($p) > strlen($s)) {
            return [];
        }

        $need = array_fill(0, 26, 0);
        $window = array_fill(0, 26, 0);
        for ($index = 0; $index < strlen($p); $index++) {
            $need[ord($p[$index]) - ord("a")]++;
        }

        $result = [];
        $left = 0;
        for ($right = 0; $right < strlen($s); $right++) {
            $window[ord($s[$right]) - ord("a")]++;
            if ($right - $left + 1 > strlen($p)) {
                $window[ord($s[$left]) - ord("a")]--;
                $left++;
            }
            if ($window === $need) {
                $result[] = $left;
            }
        }
        return $result;
    }
}
