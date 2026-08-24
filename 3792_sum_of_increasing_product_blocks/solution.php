<?php
// LeetCode 3792 - Sum of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution {
    function sumOfBlocks($n) {
        $MOD = 1000000007;
        $ans = 0;
        $k = 1;
        for ($i = 1; $i <= $n; $i++) {
            $x = 1;
            for ($j = $k; $j < $k + $i; $j++) $x = ($x * $j) % $MOD;
            $ans = ($ans + $x) % $MOD;
            $k += $i;
        }
        return $ans;
    }
}
