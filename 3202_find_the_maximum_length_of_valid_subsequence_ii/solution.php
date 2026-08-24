<?php
// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

class Solution {
    function maximumLength($nums, $k) {
        $f = [];
        for ($i = 0; $i < $k; $i++) $f[$i] = array_fill(0, $k, 0);
        $ans = 0;
        foreach ($nums as $raw) {
            $x = $raw % $k;
            for ($j = 0; $j < $k; $j++) {
                $y = ($j - $x + $k) % $k;
                $f[$x][$y] = $f[$y][$x] + 1;
                $ans = max($ans, $f[$x][$y]);
            }
        }
        return $ans;
    }
}
