<?php
// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

class Solution {
    function transformStr($s, $strs) {
        $n = strlen($s);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + ($s[$i] == '1' ? 1 : 0);
        $result = array_fill(0, count($strs), false);
        for ($i = 0; $i < count($strs); $i++) {
            $left = 0;
            $right = 0;
            $ok = true;
            for ($j = 0; $j < $n; $j++) {
                $left += ($strs[$i][$j] == '1' ? 1 : 0);
                $add = ($strs[$i][$j] != '0' ? 1 : 0);
                $right = $right + $add;
                if ($right > $prefix[$j + 1]) $right = $prefix[$j + 1];
                if ($left > $right) {
                    $ok = false;
                    break;
                }
            }
            $result[$i] = $ok && $left <= $prefix[$n] && $prefix[$n] <= $right;
        }
        return $result;
    }
}
