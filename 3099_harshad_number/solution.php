<?php
// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

class Solution {
    function sumOfTheDigitsOfHarshadNumber($x) {
        $s = 0;
        for ($y = $x; $y > 0; $y = intdiv($y, 10)) $s += $y % 10;
        return $x % $s === 0 ? $s : -1;
    }
}
