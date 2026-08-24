<?php
// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution {
    function numberOfGoodSubarraySplits($nums) {
        $MOD = 1000000007;
        $ones = [];
        for ($i = 0; $i < count($nums); $i++) if ($nums[$i] === 1) $ones[] = $i;
        if (!$ones) return 0;
        $ans = 1;
        for ($i = 1; $i < count($ones); $i++)
            $ans = $ans * ($ones[$i] - $ones[$i - 1]) % $MOD;
        return $ans;
    }
}
