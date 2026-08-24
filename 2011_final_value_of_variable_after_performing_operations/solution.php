<?php
// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution {
    /**
     * @param String[] $operations
     * @return Integer
     */
    function finalValueAfterOperations($operations) {
        $x = 0;
        foreach ($operations as $op) {
            if ($op[1] === '+') $x++;
            else $x--;
        }
        return $x;
    }
}
