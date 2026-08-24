<?php
// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isAnagram($s, $t) {
        if (strlen($s) !== strlen($t)) {
            return false;
        }
        $counts = array_fill(0, 26, 0);
        for ($index = 0, $length = strlen($s); $index < $length; $index++) {
            $counts[ord($s[$index]) - ord('a')]++;
            $counts[ord($t[$index]) - ord('a')]--;
        }
        foreach ($counts as $count) {
            if ($count !== 0) {
                return false;
            }
        }
        return true;
    }
}
