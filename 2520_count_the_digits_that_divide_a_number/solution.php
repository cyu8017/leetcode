<?php
// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution {
    function countDigits($num) {
        $ans = 0;
        $x = $num;
        while ($x > 0) {
            $d = $x % 10;
            if ($d !== 0 && $num % $d === 0) $ans++;
            $x = intdiv($x, 10);
        }
        return $ans;
    }
}
