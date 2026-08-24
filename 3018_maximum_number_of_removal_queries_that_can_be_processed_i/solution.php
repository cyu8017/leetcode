<?php
// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

class Solution {
    function maximumProcessableQueries($nums, $queries) {
        $n = count($nums);
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $n, 0);
        $m = count($queries);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $n - 1; $j >= $i; $j--) {
                if ($i > 0) {
                    $t = $f[$i - 1][$j] < $m && $nums[$i - 1] >= $queries[$f[$i - 1][$j]] ? 1 : 0;
                    $f[$i][$j] = max($f[$i][$j], $f[$i - 1][$j] + $t);
                }
                if ($j + 1 < $n) {
                    $t = $f[$i][$j + 1] < $m && $nums[$j + 1] >= $queries[$f[$i][$j + 1]] ? 1 : 0;
                    $f[$i][$j] = max($f[$i][$j], $f[$i][$j + 1] + $t);
                }
                if ($f[$i][$j] === $m) return $m;
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $t = $f[$i][$i] < $m && $nums[$i] >= $queries[$f[$i][$i]] ? 1 : 0;
            $ans = max($ans, $f[$i][$i] + $t);
        }
        return $ans;
    }
}
