<?php
// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

class Solution {
    function maxRatings($units) {
        $n = count($units[0]);
        if ($n == 1) {
            $ans = 0;
            foreach ($units as $x) $ans += $x[0];
            return $ans;
        }
        $answer = 0;
        $mn = 2147483647;
        $mn2 = 2147483647;
        foreach ($units as $x) {
            sort($x);
            $answer += $x[1];
            $mn2 = min($mn2, $x[1]);
            $mn = min($mn, $x[0]);
        }
        return $answer - ($mn2 - $mn);
    }
}
