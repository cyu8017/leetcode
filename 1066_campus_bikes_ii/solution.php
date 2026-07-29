<?php
// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

class Solution {
    /**
     * @param Integer[][] $workers
     * @param Integer[][] $bikes
     * @return Integer
     */
    function assignBikes($workers, $bikes) {
        $m = count($bikes);
        $memo = [];
        $dp = null;
        $dp = function ($i, $mask) use (&$dp, &$memo, $workers, $bikes, $m) {
            if ($i === count($workers)) {
                return 0;
            }
            $key = $i . "," . $mask;
            if (isset($memo[$key])) {
                return $memo[$key];
            }
            $best = PHP_INT_MAX;
            $wx = $workers[$i][0];
            $wy = $workers[$i][1];
            for ($b = 0; $b < $m; $b++) {
                if ($mask & (1 << $b)) {
                    continue;
                }
                $dist = abs($wx - $bikes[$b][0]) + abs($wy - $bikes[$b][1]);
                $best = min($best, $dist + $dp($i + 1, $mask | (1 << $b)));
            }
            return $memo[$key] = $best;
        };
        return $dp(0, 0);
    }
}
