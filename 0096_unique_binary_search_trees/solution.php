<?php
// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numTrees($n) {
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        for ($nodes = 1; $nodes <= $n; $nodes++) {
            for ($root = 1; $root <= $nodes; $root++) {
                $dp[$nodes] += $dp[$root - 1] * $dp[$nodes - $root];
            }
        }
        return $dp[$n];
    }
}
