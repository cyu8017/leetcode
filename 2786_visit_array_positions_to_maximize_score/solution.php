<?php
// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

class Solution {
    function maxScore($nums, $x) {
        $NEG = -1000000000000000000;
        $even = $nums[0];
        $odd = $nums[0];
        if ($nums[0] % 2 === 0) $odd = $NEG;
        else $even = $NEG;
        for ($i = 1; $i < count($nums); $i++) {
            $v = $nums[$i];
            if ($nums[$i] % 2 === 0) $even = max($even + $v, $odd + $v - $x);
            else $odd = max($odd + $v, $even + $v - $x);
        }
        return max($even, $odd);
    }
}
