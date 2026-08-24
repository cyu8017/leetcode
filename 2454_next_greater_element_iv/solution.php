<?php
// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

class Solution {
    function secondGreaterElement($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, -1);
        $stack1 = [];
        $stack2 = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while (count($stack2) && $nums[$stack2[count($stack2) - 1]] < $x) {
                $ans[array_pop($stack2)] = $x;
            }
            $tmp = [];
            while (count($stack1) && $nums[$stack1[count($stack1) - 1]] < $x) {
                $tmp[] = array_pop($stack1);
            }
            for ($j = count($tmp) - 1; $j >= 0; $j--) $stack2[] = $tmp[$j];
            $stack1[] = $i;
        }
        return $ans;
    }
}
