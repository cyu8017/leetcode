<?php
// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution {
    function partitionDisjoint($nums) {
        $n = count($nums);
        $minRight = array_fill(0, $n, 0);
        $minRight[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $minRight[$i] = min($nums[$i], $minRight[$i + 1]);
        $maxLeft = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            if ($maxLeft <= $minRight[$i]) return $i;
            $maxLeft = max($maxLeft, $nums[$i]);
        }
        return $n - 1;
    }
}
