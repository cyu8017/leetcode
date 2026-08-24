<?php
// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution {
    function minimumOperations($nums) {
        $seen = [];
        foreach ($nums as $x) if ($x > 0) $seen[$x] = true;
        return count($seen);
    }
}
