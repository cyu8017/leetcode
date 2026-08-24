<?php
// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

class Solution {
    function minOperations($nums, $k) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) $nums[$i] %= $k;
        $ans = 2147483647;
        for ($x = 0; $x < $k; $x++) {
            for ($y = 0; $y < $k; $y++) {
                if ($x == $y) continue;
                $cnt = 0;
                for ($i = 0; $i < $n; $i++) {
                    $target = ($i & 1) != 0 ? $y : $x;
                    $diff = abs($target - $nums[$i]);
                    $cnt += min($diff, $k - $diff);
                }
                $ans = min($ans, $cnt);
            }
        }
        return $ans;
    }
}
