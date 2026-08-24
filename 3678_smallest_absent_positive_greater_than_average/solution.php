<?php
// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

class Solution {
    function smallestAbsent($nums) {
        $s = [];
        $sum = 0;
        foreach ($nums as $x) {
            $s[$x] = true;
            $sum += $x;
        }
        $ans = max(1, intdiv($sum, count($nums)) + 1);
        while (isset($s[$ans])) $ans++;
        return $ans;
    }
}
