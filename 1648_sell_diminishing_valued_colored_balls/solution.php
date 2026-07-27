<?php
// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution {
    /**
     * @param Integer[] $inventory
     * @param Integer $orders
     * @return Integer
     */
    function maxProfit($inventory, $orders) {
        $MOD = 1000000007;
        rsort($inventory);
        $inventory[] = 0;
        $ans = 0;
        $len = count($inventory);
        for ($i = 0; $i < $len - 1; $i++) {
            $width = $i + 1;
            $high = $inventory[$i];
            $low = $inventory[$i + 1];
            $balls = $width * ($high - $low);
            $take = min($orders, $balls);
            $full = intdiv($take, $width);
            $rem = $take % $width;
            $bottom = $high - $full;
            $ans += $width * ($high + $bottom + 1) * $full / 2 + $rem * $bottom;
            $orders -= $take;
            if ($orders === 0) {
                break;
            }
        }
        return intval($ans % $MOD);
    }
}
