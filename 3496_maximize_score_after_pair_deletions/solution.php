<?php
// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

class Solution {
    function maximizeScore($nums) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $x) $total += $x;
        if ($n % 2 === 1) {
            $mn = $nums[0];
            foreach ($nums as $x) if ($x < $mn) $mn = $x;
            return $total - $mn;
        }
        $mn = $nums[0] + $nums[1];
        for ($i = 0; $i + 1 < $n; $i++) $mn = min($mn, $nums[$i] + $nums[$i + 1]);
        return $total - $mn;
    }
}
