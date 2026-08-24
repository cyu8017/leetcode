<?php
// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

class Solution {
    function minimumOperations($nums) {
        $ops = 0;
        for ($i = count($nums) - 2; $i >= 0; $i--) {
            if ($nums[$i] !== $nums[$i + 1]) $ops++;
        }
        return $ops;
    }
}
