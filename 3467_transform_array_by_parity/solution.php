<?php
// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

class Solution {
    function transformArray($nums) {
        for ($i = 0; $i < count($nums); $i++) $nums[$i] %= 2;
        $j = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === 0) {
                $t = $nums[$i]; $nums[$i] = $nums[$j]; $nums[$j] = $t;
                $j++;
            }
        }
        return $nums;
    }
}
