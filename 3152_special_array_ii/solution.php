<?php
// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

class Solution {
    function isArraySpecial($nums, $queries) {
        $n = count($nums);
        $d = range(0, $n - 1);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] % 2 !== $nums[$i - 1] % 2) $d[$i] = $d[$i - 1];
        }
        $ans = [];
        for ($i = 0; $i < count($queries); $i++)
            $ans[$i] = $d[$queries[$i][1]] <= $queries[$i][0];
        return $ans;
    }
}
