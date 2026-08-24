<?php
// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

class Solution {
    function splitNum($num) {
        $digits = [];
        while ($num > 0) {
            $digits[] = $num % 10;
            $num = intdiv($num, 10);
        }
        sort($digits);
        $a = 0;
        $b = 0;
        $n = count($digits);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $a = $a * 10 + $digits[$i];
            else $b = $b * 10 + $digits[$i];
        }
        return $a + $b;
    }
}
