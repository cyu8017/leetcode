<?php
// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

class Solution {
    function deleteAndEarn($nums) {
        if (count($nums) === 0) return 0;
        $maxNum = 0;
        foreach ($nums as $num) $maxNum = max($maxNum, $num);
        $points = array_fill(0, $maxNum + 1, 0);
        foreach ($nums as $num) $points[$num] += $num;
        $take = 0;
        $skip = 0;
        foreach ($points as $value) {
            $newTake = $skip + $value;
            $newSkip = max($skip, $take);
            $take = $newTake;
            $skip = $newSkip;
        }
        return max($take, $skip);
    }
}
