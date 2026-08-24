<?php
// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

class Solution {
    function minAbsoluteDifference($nums, $x) {
        if ($x === 0) {
            $ans0 = PHP_INT_MAX;
            for ($i = 1; $i < count($nums); $i++)
                $ans0 = min($ans0, abs($nums[$i] - $nums[$i - 1]));
            return $ans0;
        }
        $ans = PHP_INT_MAX;
        $arr = [];
        $insert = function($v) use (&$arr) {
            $lo = 0;
            $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($arr, $lo, 0, [$v]);
        };
        $lowerBound = function($v) use (&$arr) {
            $lo = 0;
            $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        for ($i = $x; $i < count($nums); $i++) {
            $insert($nums[$i - $x]);
            $cur = $nums[$i];
            $idx = $lowerBound($cur);
            if ($idx < count($arr)) $ans = min($ans, $arr[$idx] - $cur);
            if ($idx > 0) $ans = min($ans, $cur - $arr[$idx - 1]);
        }
        return $ans;
    }
}
