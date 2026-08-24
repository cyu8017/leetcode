<?php
// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution {
    function findIndices($nums, $indexDifference, $valueDifference) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i; $j < $n; $j++) {
                if (abs($j - $i) >= $indexDifference && abs($nums[$i] - $nums[$j]) >= $valueDifference)
                    return [$i, $j];
            }
        return [-1, -1];
    }
}
