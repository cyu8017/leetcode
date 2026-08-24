<?php
// LeetCode 3909 - Compare Sums of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

class Solution {
    function compareBitonicSums($nums) {
        $l = $nums[0];
        $r = 0;
        foreach ($nums as $x) $r += $x;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i - 1] > $nums[$i]) break;
            $l += $nums[$i];
            $r -= $nums[$i - 1];
        }
        if ($l === $r) return -1;
        if ($l > $r) return 0;
        return 1;
    }
}
