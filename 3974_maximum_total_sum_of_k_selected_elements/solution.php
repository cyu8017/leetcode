<?php
// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

class Solution {
    function maxSum($nums, $k, $mul) {
        sort($nums);
        $n = count($nums);
        $ans = 0;
        for ($i = $n - 1; $i >= $n - $k; $i--) {
            $m = max(1, $mul);
            $ans += $nums[$i] * $m;
            $mul--;
        }
        return $ans;
    }
}
