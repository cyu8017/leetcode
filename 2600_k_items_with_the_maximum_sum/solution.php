<?php
// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution {
    function kItemsWithMaximumSum($numOnes, $numZeros, $numNegOnes, $k) {
        $ans = 0;
        $take = min($numOnes, $k);
        $ans += $take;
        $k -= $take;
        $take = min($numZeros, $k);
        $k -= $take;
        $take = min($numNegOnes, $k);
        $ans -= $take;
        return $ans;
    }
}
