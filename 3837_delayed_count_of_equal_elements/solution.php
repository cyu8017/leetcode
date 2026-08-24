<?php
// LeetCode 3837 - Delayed Count of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

class Solution {
    function delayedCount($nums, $k) {
        $n = count($nums);
        $cnt = [];
        $ans = array_fill(0, $n, 0);
        for ($i = $n - $k - 2; $i >= 0; $i--) {
            $key = $nums[$i + $k + 1];
            $cnt[$key] = ($cnt[$key] ?? 0) + 1;
            $ans[$i] = $cnt[$nums[$i]] ?? 0;
        }
        return $ans;
    }
}
