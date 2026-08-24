<?php
// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

class Solution {
    function maxScore($nums) {
        $stk = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            while (count($stk) > 0 && $nums[$stk[count($stk) - 1]] <= $nums[$i]) array_pop($stk);
            $stk[] = $i;
        }
        $ans = 0;
        $cur = 0;
        foreach ($stk as $j) {
            $ans += ($j - $cur) * $nums[$j];
            $cur = $j;
        }
        return $ans;
    }
}
