<?php
// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution {
    function generateKey($num1, $num2, $num3) {
        $ans = 0;
        $mul = 1;
        for ($t = 0; $t < 4; $t++) {
            $d = min($num1 % 10, $num2 % 10, $num3 % 10);
            $ans += $d * $mul;
            $mul *= 10;
            $num1 = intdiv($num1, 10);
            $num2 = intdiv($num2, 10);
            $num3 = intdiv($num3, 10);
        }
        return $ans;
    }
}
