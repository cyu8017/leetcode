<?php
// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution {
    /**
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($cost) {
        rsort($cost);
        $ans = 0;
        for ($i = 0; $i < count($cost); $i++)
            if ($i % 3 !== 2) $ans += $cost[$i];
        return $ans;
    }
}
