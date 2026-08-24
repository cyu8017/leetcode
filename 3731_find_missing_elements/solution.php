<?php
// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

class Solution {
    function findMissingElements($nums) {
        $mn = 100;
        $mx = 0;
        $s = [];
        foreach ($nums as $x) {
            $mn = min($mn, $x);
            $mx = max($mx, $x);
            $s[$x] = true;
        }
        $ans = [];
        for ($x = $mn + 1; $x < $mx; $x++) {
            if (!isset($s[$x])) $ans[] = $x;
        }
        return $ans;
    }
}
