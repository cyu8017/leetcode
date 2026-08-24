<?php
// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

class Solution {
    function optimalDivision($nums) {
        if (count($nums) === 1) return strval($nums[0]);
        if (count($nums) === 2) return $nums[0] . "/" . $nums[1];
        $result = $nums[0] . "/(";
        for ($i = 1; $i < count($nums); ++$i) {
            if ($i > 1) $result .= "/";
            $result .= $nums[$i];
        }
        $result .= ")";
        return $result;
    }
}
