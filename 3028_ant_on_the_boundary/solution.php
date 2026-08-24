<?php
// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

class Solution {
    function returnToBoundaryCount($nums) {
        $s = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $s += $x;
            if ($s === 0) $ans++;
        }
        return $ans;
    }
}
