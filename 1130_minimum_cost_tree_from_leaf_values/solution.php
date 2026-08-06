<?php
// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function mctFromLeafValues($arr) {
        $stack = [PHP_INT_MAX];
        $ans = 0;
        foreach ($arr as $a) {
            while (end($stack) <= $a) {
                $mid = array_pop($stack);
                $ans += $mid * min(end($stack), $a);
            }
            $stack[] = $a;
        }
        while (count($stack) > 2) {
            $ans += array_pop($stack) * end($stack);
        }
        return $ans;
    }
}
