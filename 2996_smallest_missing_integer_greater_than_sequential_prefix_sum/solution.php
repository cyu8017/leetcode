<?php
// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

class Solution {
    function missingInteger($nums) {
        $sum = $nums[0];
        for ($i = 1; $i < count($nums) && $nums[$i] === $nums[$i - 1] + 1; $i++) {
            $sum += $nums[$i];
        }
        $seen = array_flip($nums);
        while (isset($seen[$sum])) $sum++;
        return $sum;
    }
}
