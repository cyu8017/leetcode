<?php
// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution {
    /**
     * @param Integer[] $stones
     * @param Integer $k
     * @return Integer
     */
    function mergeStones($stones, $k) {
        $n = count($stones);
        if (($n - 1) % ($k - 1) !== 0) {
            return -1;
        }
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $stones[$i];
        }
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($length = $k; $length <= $n; $length++) {
            for ($i = 0; $i + $length - 1 < $n; $i++) {
                $j = $i + $length - 1;
                $best = PHP_INT_MAX;
                for ($m = $i; $m < $j; $m += $k - 1) {
                    $best = min($best, $dp[$i][$m] + $dp[$m + 1][$j]);
                }
                $dp[$i][$j] = $best;
                if (($length - 1) % ($k - 1) === 0) {
                    $dp[$i][$j] += $prefix[$j + 1] - $prefix[$i];
                }
            }
        }
        return $dp[0][$n - 1];
    }
}
