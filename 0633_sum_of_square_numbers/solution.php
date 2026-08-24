<?php
// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

class Solution {
    function judgeSquareSum($c) {
        $left = 0;
        $right = intval(sqrt($c));
        while ($left <= $right) {
            $total = $left * $left + $right * $right;
            if ($total === $c) return true;
            if ($total < $c) ++$left;
            else --$right;
        }
        return false;
    }
}
