<?php
// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

class Solution {
    function ok($d, $nums, $n) {
        $prev = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] !== -1) {
                if ($prev !== -1 && abs($nums[$i] - $prev) > $d) return false;
                $prev = $nums[$i];
                continue;
            }
            $j = $i;
            while ($j < $n && $nums[$j] === -1) $j++;
            $left = $prev;
            $right = ($j < $n) ? $nums[$j] : -1;
            $gap = $j - $i;
            if ($left === -1 && $right === -1) return true;
            if ($left === -1 || $right === -1) {
                $prev = -1;
                $i = $j - 1;
                continue;
            }
            if (abs($left - $right) > $d * ($gap + 1)) return false;
            $prev = -1;
            $i = $j - 1;
        }
        return true;
    }

    function minDifference($nums) {
        $n = count($nums);
        $lo = 0;
        $hi = 1000000000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->ok($mid, $nums, $n)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
