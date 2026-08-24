<?php
// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

class Solution {
    function goodIndices($nums, $k) {
        $n = count($nums);
        $dec = array_fill(0, $n, 0);
        $inc = array_fill(0, $n, 0);
        $dec[0] = 1;
        for ($i = 1; $i < $n; $i++)
            $dec[$i] = $nums[$i] <= $nums[$i - 1] ? $dec[$i - 1] + 1 : 1;
        $inc[$n - 1] = 1;
        for ($i = $n - 2; $i >= 0; $i--)
            $inc[$i] = $nums[$i] <= $nums[$i + 1] ? $inc[$i + 1] + 1 : 1;
        $ans = [];
        for ($i = $k; $i < $n - $k; $i++) {
            if ($dec[$i - 1] >= $k && $inc[$i + 1] >= $k) $ans[] = $i;
        }
        return $ans;
    }
}
