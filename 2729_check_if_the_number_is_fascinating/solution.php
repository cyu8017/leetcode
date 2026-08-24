<?php
// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution {
    function isFascinating($n) {
        $s = (string)$n . (string)(2 * $n) . (string)(3 * $n);
        if (strlen($s) !== 9) return false;
        $cnt = array_fill(0, 10, 0);
        for ($i = 0; $i < 9; $i++) $cnt[ord($s[$i]) - 48]++;
        if ($cnt[0] !== 0) return false;
        for ($i = 1; $i <= 9; $i++) if ($cnt[$i] !== 1) return false;
        return true;
    }
}
