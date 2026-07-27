<?php
// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution {
    function minPartitions($n) {
        $best = 0;
        $len = strlen($n);
        for ($i = 0; $i < $len; $i++) {
            $best = max($best, (int)$n[$i]);
        }
        return $best;
    }
}
