<?php
// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

class Solution {
    function maximumWealth($accounts) {
        $best = 0;
        foreach ($accounts as $row) {
            $best = max($best, array_sum($row));
        }
        return $best;
    }
}
