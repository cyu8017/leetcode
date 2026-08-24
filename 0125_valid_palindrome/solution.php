<?php
// LeetCode 0125 - Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function isPalindrome($s) {
        $left = 0;
        $right = strlen($s) - 1;
        while ($left < $right) {
            while ($left < $right && !ctype_alnum($s[$left])) {
                $left++;
            }
            while ($left < $right && !ctype_alnum($s[$right])) {
                $right--;
            }
            if (strtolower($s[$left]) !== strtolower($s[$right])) {
                return false;
            }
            $left++;
            $right--;
        }
        return true;
    }
}
