<?php
// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function canPermutePalindrome($s) {
        $counts = array_fill(0, 26, 0);
        $length = strlen($s);
        for ($i = 0; $i < $length; $i++) {
            $counts[ord($s[$i]) - 97]++;
        }
        $odd = 0;
        foreach ($counts as $count) {
            if ($count % 2 !== 0) {
                $odd++;
            }
        }
        return $odd <= 1;
    }
}
