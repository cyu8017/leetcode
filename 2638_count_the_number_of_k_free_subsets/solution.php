<?php
// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

class Solution {
    function countTheNumOfKFreeSubsets($nums, $k) {
        sort($nums);
        $groups = [];
        foreach ($nums as $x) {
            $key = $x % $k;
            if (!isset($groups[$key])) $groups[$key] = [];
            $groups[$key][] = $x;
        }
        $ans = 1;
        foreach ($groups as $g) {
            $prevVal = -1;
            $prevTake = 0;
            $prevSkip = 1;
            foreach ($g as $v) {
                $skip = $prevTake + $prevSkip;
                $take = ($prevVal + $k === $v) ? $prevSkip : ($prevTake + $prevSkip);
                $prevTake = $take;
                $prevSkip = $skip;
                $prevVal = $v;
            }
            $ans *= $prevTake + $prevSkip;
        }
        return $ans;
    }
}
