<?php
// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution {
    function minimumPushes($word) {
        $n = strlen($word);
        $ans = 0;
        $k = 1;
        for ($i = 0; $i < intdiv($n, 8); $i++) {
            $ans += $k * 8;
            $k++;
        }
        $ans += $k * ($n % 8);
        return $ans;
    }
}
