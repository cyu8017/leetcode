<?php
// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isGoodArray($nums) {
        $g = $nums[0];
        foreach ($nums as $x) {
            while ($x) {
                [$g, $x] = [$x, $g % $x];
            }
            if ($g === 1) return true;
        }
        return $g === 1;
    }
}
