<?php
// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

class Solution {
    function maxScore($nums1, $nums2, $K) {
        $n = count($nums1);
        $m = count($nums2);
        $NEG = PHP_INT_MIN / 4;
        $f = [];
        for ($i = 0; $i <= $n; $i++) {
            $f[$i] = [];
            for ($j = 0; $j <= $m; $j++) $f[$i][$j] = array_fill(0, $K + 1, $NEG);
        }
        $f[0][0][0] = 0;
        for ($i = 0; $i <= $n; $i++) {
            for ($j = 0; $j <= $m; $j++) {
                for ($k = 0; $k <= $K; $k++) {
                    if ($i > 0) $f[$i][$j][$k] = max($f[$i][$j][$k], $f[$i - 1][$j][$k]);
                    if ($j > 0) $f[$i][$j][$k] = max($f[$i][$j][$k], $f[$i][$j - 1][$k]);
                    if ($i > 0 && $j > 0 && $k > 0) {
                        $f[$i][$j][$k] = max($f[$i][$j][$k], $f[$i - 1][$j - 1][$k - 1] + $nums1[$i - 1] * $nums2[$j - 1]);
                    }
                }
            }
        }
        return $f[$n][$m][$K];
    }
}
