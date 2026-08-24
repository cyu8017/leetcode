<?php
// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

class Solution {
    function maximumSum($nums) {
        $squareFree = function($x) {
            $res = 1;
            for ($p = 2; $p * $p <= $x; $p++) {
                $cnt = 0;
                while ($x % $p === 0) {
                    $x = intdiv($x, $p);
                    $cnt++;
                }
                if ($cnt % 2 === 1) $res *= $p;
            }
            if ($x > 1) $res *= $x;
            return $res;
        };
        $n = count($nums);
        $groups = [];
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $sf = $squareFree($i);
            $sum = ($groups[$sf] ?? 0) + $nums[$i - 1];
            $groups[$sf] = $sum;
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
