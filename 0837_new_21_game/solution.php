<?php
// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $maxPts
     * @return Float
     */
    function new21Game($n, $k, $maxPts) {
        if ($k === 0 || $n >= $k - 1 + $maxPts) return 1.0;
        $dp = array_fill(0, $n + 1, 0.0);
        $dp[0] = 1.0;
        $window = 1.0;
        $ans = 0.0;
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $window / $maxPts;
            if ($i < $k) $window += $dp[$i];
            else $ans += $dp[$i];
            if ($i - $maxPts >= 0 && $i - $maxPts < $k) $window -= $dp[$i - $maxPts];
        }
        return $ans;
    }
}
