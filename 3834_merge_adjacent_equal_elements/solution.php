<?php
// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

class Solution {
    function mergeAdjacent($nums) {
        $stk = [];
        foreach ($nums as $x) {
            $stk[] = $x;
            while (count($stk) > 1 && $stk[count($stk) - 1] === $stk[count($stk) - 2]) {
                $a = array_pop($stk);
                $b = array_pop($stk);
                $stk[] = $a + $b;
            }
        }
        return $stk;
    }
}
