<?php
// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution {
    /**
     * @param Integer[] $costs
     * @param Integer $coins
     * @return Integer
     */
    function maxIceCream($costs, $coins) {
        sort($costs);
        $count = 0;
        foreach ($costs as $cost) {
            if ($coins < $cost) {
                break;
            }
            $coins -= $cost;
            $count++;
        }
        return $count;
    }
}
