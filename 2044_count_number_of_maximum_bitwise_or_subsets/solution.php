<?php
// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countMaxOrSubsets($nums) {
        $maxOr = 0;
        $ans = 0;
        foreach ($nums as $x) $maxOr |= $x;
        $dfs = null;
        $dfs = function ($i, $cur) use (&$dfs, $nums, $maxOr, &$ans) {
            if ($i === count($nums)) { if ($cur === $maxOr) $ans++; return; }
            $dfs($i + 1, $cur);
            $dfs($i + 1, $cur | $nums[$i]);
        };
        $dfs(0, 0);
        return $ans;
    }
}
