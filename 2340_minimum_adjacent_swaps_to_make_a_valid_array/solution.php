<?php
// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

class Solution {
    function minimumSwaps($nums) {
        $n = count($nums);
        $minI = 0;
        $maxI = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] < $nums[$minI]) $minI = $i;
            if ($nums[$i] >= $nums[$maxI]) $maxI = $i;
        }
        $ans = $minI + ($n - 1 - $maxI);
        if ($minI > $maxI) $ans--;
        return $ans;
    }
}
