<?php
// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

class Solution {
    function maximumLength($nums, $k) {
        $n = count($nums);
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $k + 1, 0);
        $mp = [];
        $g = [];
        for ($h = 0; $h <= $k; $h++) {
            $mp[$h] = [];
            $g[$h] = [0, 0, 0];
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($h = 0; $h <= $k; $h++) {
                $f[$i][$h] = $mp[$h][$nums[$i]] ?? 0;
                if ($h > 0) {
                    if ($g[$h - 1][0] !== $nums[$i]) $f[$i][$h] = max($f[$i][$h], $g[$h - 1][1]);
                    else $f[$i][$h] = max($f[$i][$h], $g[$h - 1][2]);
                }
                $f[$i][$h]++;
                $mp[$h][$nums[$i]] = max($mp[$h][$nums[$i]] ?? 0, $f[$i][$h]);
                if ($g[$h][0] !== $nums[$i]) {
                    if ($f[$i][$h] >= $g[$h][1]) {
                        $g[$h][2] = $g[$h][1];
                        $g[$h][1] = $f[$i][$h];
                        $g[$h][0] = $nums[$i];
                    } else if ($f[$i][$h] > $g[$h][2]) {
                        $g[$h][2] = $f[$i][$h];
                    }
                } else if ($f[$i][$h] > $g[$h][1]) {
                    $g[$h][1] = $f[$i][$h];
                }
                $ans = max($ans, $f[$i][$h]);
            }
        }
        return $ans;
    }
}
