<?php
// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

class Solution {
    function minOperations($nums, $x, $k) {
        $n = count($nums);
        $minOps = array_fill(0, $n - $x + 1, 0);
        for ($i = 0; $i + $x <= $n; $i++) {
            $w = array_slice($nums, $i, $x);
            sort($w);
            $med = $w[intdiv($x - 1, 2)];
            $ops = 0;
            foreach ($w as $v) $ops += abs($v - $med);
            $minOps[$i] = $ops;
        }
        $Inf = PHP_INT_MAX >> 2;
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $k + 1, $Inf);
        $dp[$n][0] = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = 0; $j <= $k; $j++) {
                $dp[$i][$j] = $dp[$i + 1][$j];
                if ($j > 0 && $i + $x <= $n && $minOps[$i] + $dp[$i + $x][$j - 1] < $dp[$i][$j])
                    $dp[$i][$j] = $minOps[$i] + $dp[$i + $x][$j - 1];
            }
        }
        return $dp[0][$k];
    }
}
