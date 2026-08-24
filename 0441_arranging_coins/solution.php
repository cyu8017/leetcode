<?php
// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

class Solution {
    /**
     * @param int $n
     * @return int
     */
    function arrangeCoins($n) {
        return $this->arrange_coins($n);
    }

    /**
     * @param int $n
     * @return int
     */
    function arrange_coins($n) {
        $low = 0;
        $high = $n;
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if (intdiv($mid * ($mid + 1), 2) <= $n) {
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $high;
    }
}
