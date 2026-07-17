<?php
// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

class Solution {
    /**
     * @param Integer[][] $orders
     * @return Integer
     */
    function getNumberOfBacklogOrders($orders) {
        $mod = 1000000007;
        $buy = new SplMinHeap();
        $sell = new SplMinHeap();

        foreach ($orders as [$price, $amount, $orderType]) {
            if ($orderType === 0) {
                $buy->insert([-$price, $amount]);
            } else {
                $sell->insert([$price, $amount]);
            }

            while (!$buy->isEmpty() && !$sell->isEmpty()) {
                $buyTop = $buy->top();
                $sellTop = $sell->top();
                if (-$buyTop[0] < $sellTop[0]) {
                    break;
                }

                $buyPrice = -$buyTop[0];
                $buyAmount = $buyTop[1];
                $sellPrice = $sellTop[0];
                $sellAmount = $sellTop[1];
                $matched = min($buyAmount, $sellAmount);
                $buyAmount -= $matched;
                $sellAmount -= $matched;

                $buy->extract();
                $sell->extract();
                if ($buyAmount > 0) {
                    $buy->insert([-$buyPrice, $buyAmount]);
                }
                if ($sellAmount > 0) {
                    $sell->insert([$sellPrice, $sellAmount]);
                }
            }
        }

        $total = 0;
        while (!$buy->isEmpty()) {
            $total = ($total + $buy->extract()[1]) % $mod;
        }
        while (!$sell->isEmpty()) {
            $total = ($total + $sell->extract()[1]) % $mod;
        }
        return $total;
    }
}
