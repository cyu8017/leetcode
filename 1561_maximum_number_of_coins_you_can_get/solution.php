<?php

class Solution {
    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function maxCoins($piles) {
        sort($piles);
        $n = count($piles);
        $sum = 0;
        for ($i = intdiv($n, 3); $i < $n; $i += 2) {
            $sum += $piles[$i];
        }
        return $sum;
    }
}
