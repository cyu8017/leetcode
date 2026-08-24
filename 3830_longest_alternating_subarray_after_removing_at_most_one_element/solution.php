<?php
// LeetCode 3830 - Longest Alternating Subarray After Removing at Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

class Solution {
    function longestAlternating($nums) {
        $n = count($nums);
        $l1 = array_fill(0, $n, 1);
        $l2 = array_fill(0, $n, 1);
        $r1 = array_fill(0, $n, 1);
        $r2 = array_fill(0, $n, 1);
        $ans = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] < $nums[$i]) $l1[$i] = $l2[$i - 1] + 1;
            else if ($nums[$i - 1] > $nums[$i]) $l2[$i] = $l1[$i - 1] + 1;
            $ans = max($ans, max($l1[$i], $l2[$i]));
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i + 1] > $nums[$i]) $r1[$i] = $r2[$i + 1] + 1;
            else if ($nums[$i + 1] < $nums[$i]) $r2[$i] = $r1[$i + 1] + 1;
        }
        for ($i = 1; $i < $n - 1; $i++) {
            if ($nums[$i - 1] < $nums[$i + 1]) $ans = max($ans, $l2[$i - 1] + $r2[$i + 1]);
            else if ($nums[$i - 1] > $nums[$i + 1]) $ans = max($ans, $l1[$i - 1] + $r1[$i + 1]);
        }
        return $ans;
    }
}
