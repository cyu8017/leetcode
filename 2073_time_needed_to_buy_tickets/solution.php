<?php
// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution {
    /**
     * @param Integer[] $tickets
     * @param Integer $k
     * @return Integer
     */
    function timeRequiredToBuy($tickets, $k) {
        $ans = 0;
        $n = count($tickets);
        for ($i = 0; $i < $n; $i++) {
            if ($i <= $k) $ans += min($tickets[$i], $tickets[$k]);
            else $ans += min($tickets[$i], $tickets[$k] - 1);
        }
        return $ans;
    }
}
