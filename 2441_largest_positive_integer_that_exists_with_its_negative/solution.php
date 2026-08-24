<?php
// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution {
    function findMaxK($nums) {
        $seen = [];
        $ans = -1;
        foreach ($nums as $x) {
            $seen[$x] = true;
            if ($x > 0 && isset($seen[-$x]) && $x > $ans) $ans = $x;
            if ($x < 0 && isset($seen[-$x]) && -$x > $ans) $ans = -$x;
        }
        return $ans;
    }
}
