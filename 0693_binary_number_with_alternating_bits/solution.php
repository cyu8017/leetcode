<?php
// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution {
    function hasAlternatingBits($n) {
        $x = $n ^ ($n >> 1);
        return ($x & ($x + 1)) === 0;
    }
}
