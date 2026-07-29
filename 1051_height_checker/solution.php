<?php
// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

class Solution {
    /**
     * @param Integer[] $heights
     * @return Integer
     */
    function heightChecker($heights) {
        $sorted = $heights;
        sort($sorted);
        $ans = 0;
        foreach ($heights as $i => $h) {
            if ($h !== $sorted[$i]) {
                $ans++;
            }
        }
        return $ans;
    }
}
