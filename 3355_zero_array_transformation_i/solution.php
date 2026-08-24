<?php
// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

class Solution {
    function isZeroArray($nums, $queries) {
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        foreach ($queries as $q) {
            $diff[$q[0]]++;
            $diff[$q[1] + 1]--;
        }
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            if ($cur < $nums[$i]) return false;
        }
        return true;
    }
}
