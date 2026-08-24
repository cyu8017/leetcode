<?php
// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

class Solution {
    function buyChoco($prices, $money) {
        sort($prices);
        $cost = $prices[0] + $prices[1];
        return $cost <= $money ? $money - $cost : $money;
    }
}
