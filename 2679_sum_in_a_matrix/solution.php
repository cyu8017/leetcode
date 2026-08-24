<?php
// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

class Solution {
    function matrixSum($nums) {
        foreach ($nums as &$row) sort($row);
        unset($row);
        $ans = 0;
        $n = count($nums[0]);
        for ($j = 0; $j < $n; $j++) {
            $mx = 0;
            foreach ($nums as $row) $mx = max($mx, $row[$j]);
            $ans += $mx;
        }
        return $ans;
    }
}
