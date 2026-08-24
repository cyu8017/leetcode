<?php
// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

class Solution {
    function makePrefSumNonNegative($nums) {
        $h = new SplPriorityQueue();
        $sum = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $sum += $x;
            if ($x < 0) $h->insert($x, -$x);
            if ($sum < 0) {
                $worst = $h->extract();
                $sum -= $worst;
                $ans++;
            }
        }
        return $ans;
    }
}
