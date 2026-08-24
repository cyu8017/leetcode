<?php
// LeetCode 3723 - Maximize Sum of Squares of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

class Solution {
    function maxSumOfSquares($num, $sum) {
        if ($num * 9 < $sum) return "";
        $k = intdiv($sum, 9);
        $s = $sum % 9;
        $ans = str_repeat('9', $k);
        if ($s > 0) $ans .= chr(48 + $s);
        while (strlen($ans) < $num) $ans .= '0';
        return $ans;
    }
}
