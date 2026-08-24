<?php
// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

class Solution {
    function maximumStrength($nums, $k) {
        $n = count($nums);
        $INF = -4000000000000000000;
        $f = [];
        for ($i = 0; $i <= $n; $i++) {
            $f[$i] = [];
            for ($j = 0; $j <= $k; $j++) $f[$i][$j] = [$INF, $INF];
        }
        $f[0][0][0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            for ($j = 0; $j <= $k; $j++) {
                $sign = ($j & 1) !== 0 ? 1 : -1;
                $val = $sign * $x * ($k - $j + 1);
                $f[$i][$j][0] = max($f[$i - 1][$j][0], $f[$i - 1][$j][1]);
                $f[$i][$j][1] = max($f[$i][$j][1], $f[$i - 1][$j][1] + $val);
                if ($j > 0) {
                    $t = max($f[$i - 1][$j - 1][0], $f[$i - 1][$j - 1][1]) + $val;
                    $f[$i][$j][1] = max($f[$i][$j][1], $t);
                }
            }
        }
        return max($f[$n][$k][0], $f[$n][$k][1]);
    }
}
