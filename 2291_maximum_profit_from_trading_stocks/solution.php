<?php
// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

class Solution {
    function solve($present, $future, $budget) {
        $n = count($present);
        $dp = array_fill(0, $budget + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $profit = $future[$i] - $present[$i];
            if ($profit <= 0) continue;
            $cost = $present[$i];
            for ($b = $budget; $b >= $cost; $b--)
                $dp[$b] = max($dp[$b], $dp[$b - $cost] + $profit);
        }
        return $dp[$budget];
    }
}
