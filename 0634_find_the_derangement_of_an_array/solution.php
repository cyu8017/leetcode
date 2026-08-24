<?php
// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

class Solution {
    function findDerangement($n) {
        $mod = 1000000007;
        if ($n === 1) return 0;
        $prev2 = 0;
        $prev1 = 1;
        for ($size = 3; $size <= $n; ++$size) {
            $next = (($size - 1) * ($prev1 + $prev2)) % $mod;
            $prev2 = $prev1;
            $prev1 = $next;
        }
        return $prev1;
    }
}
