<?php
// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

class Solution {
    function applyOperations($nums) {
        $n = count($nums);
        $a = $nums;
        for ($i = 0; $i + 1 < $n; $i++) {
            if ($a[$i] === $a[$i + 1]) {
                $a[$i] *= 2;
                $a[$i + 1] = 0;
            }
        }
        $ans = array_fill(0, $n, 0);
        $j = 0;
        foreach ($a as $x) if ($x !== 0) $ans[$j++] = $x;
        return $ans;
    }
}
