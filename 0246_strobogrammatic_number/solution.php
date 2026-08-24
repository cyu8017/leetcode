<?php
// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

class Solution {
    /**
     * @param String $num
     * @return Boolean
     */
    function isStrobogrammatic($num) {
        $mapping = [
            "0" => "0",
            "1" => "1",
            "6" => "9",
            "8" => "8",
            "9" => "6",
        ];
        $left = 0;
        $right = strlen($num) - 1;
        while ($left <= $right) {
            if ($mapping[$num[$left]] !== $num[$right]) {
                return false;
            }
            $left++;
            $right--;
        }
        return true;
    }
}
