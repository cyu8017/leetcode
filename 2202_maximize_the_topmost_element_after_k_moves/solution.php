<?php
// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution {
    function maximumTop($nums, $k) {
        $n = count($nums);
        if ($n === 1) return $k % 2 !== 0 ? -1 : $nums[0];
        if ($k === 0) return $nums[0];
        $ans = -1;
        $limit = min($k - 1, $n);
        for ($i = 0; $i < $limit; $i++) $ans = max($ans, $nums[$i]);
        if ($k < $n) $ans = max($ans, $nums[$k]);
        return $ans;
    }
}
