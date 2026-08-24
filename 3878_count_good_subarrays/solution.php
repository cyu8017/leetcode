<?php
// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

class Solution {
    function countGoodSubarrays($nums) {
        $n = count($nums);
        $l = array_fill(0, $n, -1);
        $stk = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while (count($stk) > 0 && $nums[$stk[count($stk) - 1]] < $x && ($nums[$stk[count($stk) - 1]] | $x) === $x) {
                array_pop($stk);
            }
            if (count($stk) > 0) $l[$i] = $stk[count($stk) - 1];
            $stk[] = $i;
        }
        $r = array_fill(0, $n, $n);
        $stk = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($stk) > 0 && ($nums[$stk[count($stk) - 1]] | $nums[$i]) === $nums[$i]) {
                array_pop($stk);
            }
            if (count($stk) > 0) $r[$i] = $stk[count($stk) - 1];
            $stk[] = $i;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += ($i - $l[$i]) * ($r[$i] - $i);
        }
        return $ans;
    }
}
