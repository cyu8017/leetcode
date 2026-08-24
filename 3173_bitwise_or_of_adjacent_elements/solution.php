<?php
// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

class Solution {
    function orArray($nums) {
        $n = count($nums);
        $ans = [];
        for ($i = 1; $i < $n; $i++) $ans[] = $nums[$i] | $nums[$i - 1];
        return $ans;
    }
}
