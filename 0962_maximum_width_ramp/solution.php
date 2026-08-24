<?php
// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

class Solution {
    function maxWidthRamp($nums) {
        $stack = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!$stack || $nums[$stack[count($stack) - 1]] > $nums[$i]) $stack[] = $i;
        }
        $ans = 0;
        for ($j = $n - 1; $j >= 0; $j--) {
            while ($stack && $nums[$stack[count($stack) - 1]] <= $nums[$j]) {
                $ans = max($ans, $j - $stack[count($stack) - 1]);
                array_pop($stack);
            }
        }
        return $ans;
    }
}
