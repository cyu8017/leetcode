<?php
// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

class Solution {
    function maximumSubarrayXor($nums, $queries) {
        $n = count($nums);
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $f[$i][$i] = $nums[$i];
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i + $length - 1 < $n; $i++) {
                $j = $i + $length - 1;
                $f[$i][$j] = $f[$i][$j - 1] ^ $f[$i + 1][$j];
            }
        }
        $best = [];
        for ($i = 0; $i < $n; $i++) $best[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $best[$i][$i] = $f[$i][$i];
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i + $length - 1 < $n; $i++) {
                $j = $i + $length - 1;
                $best[$i][$j] = max($f[$i][$j], $best[$i][$j - 1], $best[$i + 1][$j]);
            }
        }
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) $ans[$i] = $best[$queries[$i][0]][$queries[$i][1]];
        return $ans;
    }
}
