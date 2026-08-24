<?php
// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countElements($nums) {
        $mn = $nums[0];
        $mx = $nums[0];
        foreach ($nums as $x) {
            $mn = min($mn, $x);
            $mx = max($mx, $x);
        }
        $ans = 0;
        foreach ($nums as $x) if ($x > $mn && $x < $mx) $ans++;
        return $ans;
    }
}
