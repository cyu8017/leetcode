<?php
// LeetCode 3751 - Total Waviness of Numbers in Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution {
    function totalWaviness($num1, $num2) {
        $F = function($x) {
            $nums = [];
            while ($x > 0) {
                $nums[] = $x % 10;
                $x = intdiv($x, 10);
            }
            $m = count($nums);
            if ($m < 3) return 0;
            $s = 0;
            for ($i = 1; $i < $m - 1; $i++) {
                if (($nums[$i] > $nums[$i - 1] && $nums[$i] > $nums[$i + 1]) ||
                    ($nums[$i] < $nums[$i - 1] && $nums[$i] < $nums[$i + 1])) $s++;
            }
            return $s;
        };
        $ans = 0;
        for ($x = $num1; $x <= $num2; $x++) $ans += $F($x);
        return $ans;
    }
}
