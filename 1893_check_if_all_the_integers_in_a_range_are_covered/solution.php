<?php
// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution {
    /**
     * @param Integer[][] $ranges
     * @param Integer $left
     * @param Integer $right
     * @return Boolean
     */
    function isCovered($ranges, $left, $right) {
        $covered = array_fill(0, 51, false);
        foreach ($ranges as $range) {
            [$start, $end] = $range;
            for ($value = $start; $value <= $end; $value++) {
                $covered[$value] = true;
            }
        }
        for ($value = $left; $value <= $right; $value++) {
            if (!$covered[$value]) {
                return false;
            }
        }
        return true;
    }
}
