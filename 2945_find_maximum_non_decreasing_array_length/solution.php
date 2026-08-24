<?php
// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

class Solution {
    function findMaximumLength($nums) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        $last = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $dp = array_fill(0, $n + 1, 0);
        $dq = [[0, 0]];
        for ($i = 1; $i <= $n; $i++) {
            while (count($dq) > 1 && $dq[1][1] <= $pref[$i]) array_shift($dq);
            $j = $dq[0][0];
            $dp[$i] = $dp[$j] + 1;
            $last[$i] = $pref[$i] - $pref[$j];
            $val = $pref[$i] + $last[$i];
            while (count($dq) && $dq[count($dq) - 1][1] >= $val) array_pop($dq);
            $dq[] = [$i, $val];
        }
        return $dp[$n];
    }
}
