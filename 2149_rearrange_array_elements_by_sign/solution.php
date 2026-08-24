<?php
// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function rearrangeArray($nums) {
        $ans = array_fill(0, count($nums), 0);
        $pos = 0;
        $neg = 1;
        foreach ($nums as $x) {
            if ($x > 0) { $ans[$pos] = $x; $pos += 2; }
            else { $ans[$neg] = $x; $neg += 2; }
        }
        return $ans;
    }
}
