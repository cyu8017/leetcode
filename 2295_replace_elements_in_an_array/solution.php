<?php
// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

class Solution {
    function arrayChange($nums, $operations) {
        $pos = [];
        for ($i = 0; $i < count($nums); $i++) $pos[$nums[$i]] = $i;
        foreach ($operations as $op) {
            $i = $pos[$op[0]];
            $nums[$i] = $op[1];
            unset($pos[$op[0]]);
            $pos[$op[1]] = $i;
        }
        return $nums;
    }
}
