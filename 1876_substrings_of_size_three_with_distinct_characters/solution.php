<?php
// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countGoodSubstrings($s) {
        $n = strlen($s);
        if ($n < 3) {
            return 0;
        }

        $count = 0;
        for ($i = 0; $i <= $n - 3; $i++) {
            $window = substr($s, $i, 3);
            if (count(array_unique(str_split($window))) === 3) {
                $count++;
            }
        }
        return $count;
    }
}
