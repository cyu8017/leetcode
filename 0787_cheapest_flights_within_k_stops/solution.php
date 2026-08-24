<?php
// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $flights
     * @param Integer $src
     * @param Integer $dst
     * @param Integer $k
     * @return Integer
     */
    function findCheapestPrice($n, $flights, $src, $dst, $k) {
        $INF = intdiv(PHP_INT_MAX, 4);
        $dist = array_fill(0, $n, $INF);
        $dist[$src] = 0;
        for ($i = 0; $i <= $k; $i++) {
            $nxt = $dist;
            foreach ($flights as $f) {
                $u = $f[0];
                $v = $f[1];
                $price = $f[2];
                if ($dist[$u] !== $INF && $dist[$u] + $price < $nxt[$v]) {
                    $nxt[$v] = $dist[$u] + $price;
                }
            }
            $dist = $nxt;
        }
        return $dist[$dst] === $INF ? -1 : $dist[$dst];
    }
}
