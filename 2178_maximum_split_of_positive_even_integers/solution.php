<?php
// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

class Solution {
    /**
     * @param Integer $finalSum
     * @return Integer[]
     */
    function maximumEvenSplit($finalSum) {
        if ($finalSum % 2 !== 0) return [];
        $ans = [];
        for ($x = 2; $x <= $finalSum; $x += 2) {
            $ans[] = $x;
            $finalSum -= $x;
        }
        $ans[count($ans) - 1] += $finalSum;
        return $ans;
    }
}
