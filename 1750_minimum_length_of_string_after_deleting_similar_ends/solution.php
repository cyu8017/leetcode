<?php
// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minimumLength($s) {
        $left = 0;
        $right = strlen($s) - 1;
        while ($left < $right && $s[$left] === $s[$right]) {
            $ch = $s[$left];
            while ($left <= $right && $s[$left] === $ch) {
                $left++;
            }
            while ($left <= $right && $s[$right] === $ch) {
                $right--;
            }
        }
        return $right - $left + 1;
    }
}
