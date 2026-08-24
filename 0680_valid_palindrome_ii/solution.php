<?php
// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

class Solution {
    function validPalindrome($s) {
        $isPalindrome = function ($left, $right) use ($s) {
            while ($left < $right) {
                if ($s[$left] !== $s[$right]) return false;
                $left++;
                $right--;
            }
            return true;
        };
        $left = 0;
        $right = strlen($s) - 1;
        while ($left < $right) {
            if ($s[$left] !== $s[$right]) {
                return $isPalindrome($left + 1, $right) || $isPalindrome($left, $right - 1);
            }
            $left++;
            $right--;
        }
        return true;
    }
}
