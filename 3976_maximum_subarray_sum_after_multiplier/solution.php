<?php
// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

class Solution {
    function maxSubarraySum($nums, $k) {
        $n = count($nums);
        $inf = -PHP_INT_MAX / 4;
        $f = array_fill(0, $n + 1, array_fill(0, 4, $inf));
        $f[0][0] = 0;
        $ans = $inf;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            $f[$i][0] = max($f[$i - 1][0], 0) + $x;
            $f[$i][1] = max(max($f[$i - 1][0], $f[$i - 1][1]), 0) + $x * $k;
            $f[$i][2] = max(max($f[$i - 1][0], $f[$i - 1][2]), 0) + intdiv($x, $k);
            $f[$i][3] = max(max($f[$i - 1][1], $f[$i - 1][2]), $f[$i - 1][3]) + $x;
            $ans = max($ans, max(max($f[$i][0], $f[$i][1]), max($f[$i][2], $f[$i][3])));
        }
        return $ans;
    }
}
