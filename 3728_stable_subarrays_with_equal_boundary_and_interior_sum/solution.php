<?php
// LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

class Solution {
    function countStableSubarrays($capacity) {
        $n = count($capacity);
        $s = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) $s[$i] = $s[$i - 1] + $capacity[$i - 1];
        $cnt = [];
        $ans = 0;
        for ($r = 2; $r < $n; $r++) {
            $l = $r - 2;
            $keyL = $capacity[$l] . "#" . ($capacity[$l] + $s[$l + 1]);
            if (!isset($cnt[$keyL])) $cnt[$keyL] = 0;
            $cnt[$keyL]++;
            $keyR = $capacity[$r] . "#" . $s[$r];
            $ans += isset($cnt[$keyR]) ? $cnt[$keyR] : 0;
        }
        return $ans;
    }
}
