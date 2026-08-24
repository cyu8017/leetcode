<?php
// LeetCode 3779 - Minimum Number of Operations to Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

class Solution {
    function minOperations($nums) {
        $st = [];
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            if (isset($st[$nums[$i]])) return intdiv($i, 3) + 1;
            $st[$nums[$i]] = true;
        }
        return 0;
    }
}
