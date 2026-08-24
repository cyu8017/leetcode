<?php
// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $key
     * @return Integer
     */
    function mostFrequent($nums, $key) {
        $freq = [];
        $best = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i + 1 < $n; $i++) {
            if ($nums[$i] === $key) {
                $v = ($freq[$nums[$i + 1]] ?? 0) + 1;
                $freq[$nums[$i + 1]] = $v;
                if ($v > $best) { $best = $v; $ans = $nums[$i + 1]; }
            }
        }
        return $ans;
    }
}
