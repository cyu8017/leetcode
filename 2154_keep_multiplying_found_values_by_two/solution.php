<?php
// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $original
     * @return Integer
     */
    function findFinalValue($nums, $original) {
        $have = array_fill_keys($nums, true);
        while (isset($have[$original])) $original *= 2;
        return $original;
    }
}
