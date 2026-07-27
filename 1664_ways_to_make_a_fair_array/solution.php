<?php
// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution {
    function waysToMakeFair($nums) {
        $te = 0;
        $to = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2) $to += $nums[$i];
            else $te += $nums[$i];
        }
        $le = 0;
        $lo = 0;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i % 2) $to -= $x;
            else $te -= $x;
            if ($le + $to === $lo + $te) $ans++;
            if ($i % 2) $lo += $x;
            else $le += $x;
        }
        return $ans;
    }
}
