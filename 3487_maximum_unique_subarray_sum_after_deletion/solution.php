<?php
// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution {
    function maxSum($nums) {
        $seen = [];
        $sum = 0;
        $hasPos = false;
        $maxNeg = -1e9;
        foreach ($nums as $x) {
            if ($x < 0) {
                if ($x > $maxNeg) $maxNeg = $x;
                continue;
            }
            $hasPos = true;
            if (!isset($seen[$x])) {
                $seen[$x] = true;
                $sum += $x;
            }
        }
        return $hasPos ? $sum : $maxNeg;
    }
}
