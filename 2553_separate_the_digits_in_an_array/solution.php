<?php
// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution {
    function separateDigits($nums) {
        $ans = [];
        foreach ($nums as $num) {
            $digits = [];
            while ($num > 0) {
                $digits[] = $num % 10;
                $num = intdiv($num, 10);
            }
            for ($i = count($digits) - 1; $i >= 0; $i--) $ans[] = $digits[$i];
        }
        return $ans;
    }
}
