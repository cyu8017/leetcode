<?php
// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function bestRotation($nums) {
        $n = count($nums);
        $change = array_fill(0, $n, 1);
        for ($i = 0; $i < $n; $i++) $change[($i - $nums[$i] + 1 + $n) % $n] -= 1;
        for ($i = 1; $i < $n; $i++) $change[$i] += $change[$i - 1];
        $best = 0;
        for ($i = 1; $i < $n; $i++) if ($change[$i] > $change[$best]) $best = $i;
        return $best;
    }
}
