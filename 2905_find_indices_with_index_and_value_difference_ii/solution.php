<?php
// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution {
    function findIndices($nums, $indexDifference, $valueDifference) {
        $n = count($nums);
        $minIdx = 0;
        $maxIdx = 0;
        for ($j = $indexDifference; $j < $n; $j++) {
            $i = $j - $indexDifference;
            if ($nums[$i] < $nums[$minIdx]) $minIdx = $i;
            if ($nums[$i] > $nums[$maxIdx]) $maxIdx = $i;
            if ($nums[$j] - $nums[$minIdx] >= $valueDifference) return [$minIdx, $j];
            if ($nums[$maxIdx] - $nums[$j] >= $valueDifference) return [$maxIdx, $j];
        }
        return [-1, -1];
    }
}
