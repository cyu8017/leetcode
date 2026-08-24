<?php
// LeetCode 2481 - Minimum Cuts to Divide a Circle
// https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution {
    function numberOfCuts($n) {
        if ($n === 1) return 0;
        if ($n % 2 === 0) return intdiv($n, 2);
        return $n;
    }
}
