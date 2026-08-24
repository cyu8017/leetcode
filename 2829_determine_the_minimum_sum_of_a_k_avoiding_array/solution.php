<?php
// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution {
    function minimumSum($n, $k) {
        $used = [];
        $sum = 0;
        $x = 1;
        while (count($used) < $n) {
            if (!isset($used[$k - $x])) {
                $used[$x] = true;
                $sum += $x;
            }
            $x++;
        }
        return $sum;
    }
}
