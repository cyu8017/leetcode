<?php
// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

class Solution {
    function minOperations($nums) {
        $f = [];
        $f[$nums[0]] = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $x = $nums[$i];
            $g = [];
            foreach ($f as $pre => $s) {
                $cur = (int)ceil($x / $pre) * $pre;
                while ($cur <= 100) {
                    $val = $s + ($cur - $x);
                    if (!isset($g[$cur]) || $g[$cur] > $val) $g[$cur] = $val;
                    $cur += $pre;
                }
            }
            $f = $g;
        }
        $ans = PHP_INT_MAX;
        foreach ($f as $v) $ans = min($ans, $v);
        return $ans;
    }
}
