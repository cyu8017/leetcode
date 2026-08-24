<?php
// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution {
    function findUnsortedSubarray($nums) {
        $n = count($nums);
        $left = -1;
        $right = -2;
        $maxSeen = $nums[0];
        $minSeen = $nums[$n - 1];
        for ($i = 0; $i < $n; ++$i) {
            $maxSeen = max($maxSeen, $nums[$i]);
            if ($nums[$i] < $maxSeen) $right = $i;
            $j = $n - 1 - $i;
            $minSeen = min($minSeen, $nums[$j]);
            if ($nums[$j] > $minSeen) $left = $j;
        }
        return $right - $left + 1;
    }
}
