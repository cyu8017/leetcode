<?php

class Solution {
    /**
     * @param Integer[] $locations
     * @param Integer $start
     * @param Integer $finish
     * @param Integer $fuel
     * @return Integer
     */
    function countRoutes($locations, $start, $finish, $fuel) {
        $mod = 1000000007;
        $memo = [];

        $dp = function ($city, $left) use (&$dp, &$memo, $locations, $finish, $mod) {
            $key = $city . ',' . $left;
            if (isset($memo[$key])) {
                return $memo[$key];
            }
            $total = ($city === $finish) ? 1 : 0;
            $n = count($locations);
            for ($nxt = 0; $nxt < $n; $nxt++) {
                if ($nxt === $city) {
                    continue;
                }
                $cost = abs($locations[$city] - $locations[$nxt]);
                if ($cost <= $left) {
                    $total = ($total + $dp($nxt, $left - $cost)) % $mod;
                }
            }
            return $memo[$key] = $total;
        };

        return $dp($start, $fuel);
    }
}
