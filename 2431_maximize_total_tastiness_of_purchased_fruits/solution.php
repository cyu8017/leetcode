<?php
// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

class Solution {
    function maxTastiness($price, $tastiness, $maxAmount, $maxCoupons) {
        $n = count($price);
        $NEG = intdiv(-2147483647, 2);
        $dp = [];
        for ($a = 0; $a <= $maxAmount; $a++) $dp[] = array_fill(0, $maxCoupons + 1, $NEG);
        $dp[0][0] = 0;
        for ($i = 0; $i < $n; $i++) {
            $p = $price[$i];
            $t = $tastiness[$i];
            for ($a = $maxAmount; $a >= 0; $a--) {
                for ($c = $maxCoupons; $c >= 0; $c--) {
                    if ($dp[$a][$c] < 0) continue;
                    if ($a + $p <= $maxAmount) $dp[$a + $p][$c] = max($dp[$a + $p][$c], $dp[$a][$c] + $t);
                    $half = intdiv($p, 2);
                    if ($c + 1 <= $maxCoupons && $a + $half <= $maxAmount)
                        $dp[$a + $half][$c + 1] = max($dp[$a + $half][$c + 1], $dp[$a][$c] + $t);
                }
            }
        }
        $ans = 0;
        for ($a = 0; $a <= $maxAmount; $a++)
            for ($c = 0; $c <= $maxCoupons; $c++)
                if ($dp[$a][$c] > $ans) $ans = $dp[$a][$c];
        return $ans;
    }
}
