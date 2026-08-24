<?php
// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

class Solution {
    function maxTransactions($transactions) {
        $tm = [];
        $ans = count($transactions);
        $s = 0;
        foreach ($transactions as $x) {
            $s += $x;
            if (!isset($tm[$x])) $tm[$x] = 0;
            $tm[$x]++;
            while ($s < 0) {
                $y = null;
                foreach ($tm as $k => $_) {
                    if ($y === null || $k < $y) $y = $k;
                }
                $s -= $y;
                $ans--;
                $c = $tm[$y];
                if ($c === 1) unset($tm[$y]);
                else $tm[$y] = $c - 1;
            }
        }
        return $ans;
    }
}
