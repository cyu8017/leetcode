<?php
// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

class Solution {
    function maxValue($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $preMax = array_fill(0, $n, 0);
        $preMax[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) $preMax[$i] = max($preMax[$i - 1], $nums[$i]);
        $sufMin = 1073741823;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($preMax[$i] > $sufMin) $ans[$i] = $ans[$i + 1];
            else $ans[$i] = $preMax[$i];
            $sufMin = min($sufMin, $nums[$i]);
        }
        return $ans;
    }
}
