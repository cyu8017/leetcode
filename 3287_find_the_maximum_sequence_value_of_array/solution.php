<?php
// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

class Solution {
    function maxValue($nums, $k) {
        $n = count($nums);
        $MAX = 128;
        $left = [];
        for ($i = 0; $i <= $n; $i++) {
            $left[$i] = [];
            for ($j = 0; $j <= $k; $j++) $left[$i][$j] = array_fill(0, $MAX, false);
        }
        $left[0][0][0] = true;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j <= $k; $j++) {
                for ($v = 0; $v < $MAX; $v++) {
                    if (!$left[$i][$j][$v]) continue;
                    $left[$i + 1][$j][$v] = true;
                    if ($j < $k) $left[$i + 1][$j + 1][$v | $nums[$i]] = true;
                }
            }
        }
        $right = [];
        for ($i = 0; $i <= $n; $i++) {
            $right[$i] = [];
            for ($j = 0; $j <= $k; $j++) $right[$i][$j] = array_fill(0, $MAX, false);
        }
        $right[$n][0][0] = true;
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = 0; $j <= $k; $j++) {
                for ($v = 0; $v < $MAX; $v++) {
                    if (!$right[$i + 1][$j][$v]) continue;
                    $right[$i][$j][$v] = true;
                    if ($j < $k) $right[$i][$j + 1][$v | $nums[$i]] = true;
                }
            }
        }
        $ans = 0;
        for ($mid = $k; $mid + $k <= $n; $mid++) {
            for ($a = 0; $a < $MAX; $a++) {
                if (!$left[$mid][$k][$a]) continue;
                for ($b = 0; $b < $MAX; $b++) {
                    if ($right[$mid][$k][$b] && ($a ^ $b) > $ans) $ans = $a ^ $b;
                }
            }
        }
        return $ans;
    }
}
