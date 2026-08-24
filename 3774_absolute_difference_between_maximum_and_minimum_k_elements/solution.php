<?php
// LeetCode 3774 - Absolute Difference Between Maximum and Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution {
    function absDifference($nums, $k) {
        $a = $nums;
        sort($a);
        $ans = 0;
        $n = count($a);
        for ($i = 0; $i < $k; $i++) $ans += $a[$n - $i - 1] - $a[$i];
        return $ans;
    }
}
