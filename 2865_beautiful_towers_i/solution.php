<?php
// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

class Solution {
    function maximumSumOfHeights($heights) {
        $n = count($heights);
        $ans = 0;
        for ($peak = 0; $peak < $n; $peak++) {
            $sum = $heights[$peak];
            $mn = $heights[$peak];
            for ($i = $peak - 1; $i >= 0; $i--) {
                if ($heights[$i] < $mn) $mn = $heights[$i];
                $sum += $mn;
            }
            $mn = $heights[$peak];
            for ($i = $peak + 1; $i < $n; $i++) {
                if ($heights[$i] < $mn) $mn = $heights[$i];
                $sum += $mn;
            }
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
