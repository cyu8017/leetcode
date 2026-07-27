<?php
// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution {
    function mostCompetitive($nums, $k) {
        $st = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while ($st && $st[count($st) - 1] > $x && count($st) - 1 + $n - $i >= $k) {
                array_pop($st);
            }
            if (count($st) < $k) $st[] = $x;
        }
        return $st;
    }
}
