<?php
// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution {
    /**
     * @param String $binary
     * @return String
     */
    function maximumBinaryString($binary) {
        $zeros = substr_count($binary, '0');
        if ($zeros <= 1) {
            return $binary;
        }
        $first = strpos($binary, '0');
        $n = strlen($binary);
        return str_repeat('1', $first + $zeros - 1) . '0' . str_repeat('1', $n - $first - $zeros);
    }
}
