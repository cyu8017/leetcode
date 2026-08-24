<?php
// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfBeauties($nums) {
        $n = count($nums);
        $prefixMax = array_fill(0, $n, 0);
        $suffixMin = array_fill(0, $n, 0);
        $prefixMax[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) $prefixMax[$i] = max($prefixMax[$i - 1], $nums[$i]);
        $suffixMin[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $suffixMin[$i] = min($suffixMin[$i + 1], $nums[$i]);
        $ans = 0;
        for ($i = 1; $i < $n - 1; $i++) {
            if ($prefixMax[$i - 1] < $nums[$i] && $nums[$i] < $suffixMin[$i + 1]) $ans += 2;
            else if ($nums[$i - 1] < $nums[$i] && $nums[$i] < $nums[$i + 1]) $ans++;
        }
        return $ans;
    }
}
