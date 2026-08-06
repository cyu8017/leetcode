<?php
// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

class Solution {
    /**
     * @param String[] $transactions
     * @return String[]
     */
    function invalidTransactions($transactions) {
        $parsed = [];
        foreach ($transactions as $t) {
            [$name, $time, $amount, $city] = explode(',', $t);
            $parsed[] = [$name, (int)$time, (int)$amount, $city, $t];
        }
        $invalid = [];
        $m = count($parsed);
        for ($i = 0; $i < $m; $i++) {
            [$name, $time, $amount, $city, $raw] = $parsed[$i];
            if ($amount > 1000) $invalid[$raw] = true;
            for ($j = 0; $j < $m; $j++) {
                if ($i === $j) continue;
                [$name2, $time2, , $city2, $raw2] = $parsed[$j];
                if ($name === $name2 && $city !== $city2 && abs($time - $time2) <= 60) {
                    $invalid[$raw] = true;
                    $invalid[$raw2] = true;
                }
            }
        }
        return array_keys($invalid);
    }
}
