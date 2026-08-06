<?php

class Solution {
    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minCostConnectPoints($points) {
        $n = count($points);
        $used = array_fill(0, $n, false);
        $dist = array_fill(0, $n, 1000000000);
        $dist[0] = 0;
        $answer = 0;

        for ($k = 0; $k < $n; $k++) {
            $u = -1;
            for ($i = 0; $i < $n; $i++) {
                if (!$used[$i] && ($u === -1 || $dist[$i] < $dist[$u])) {
                    $u = $i;
                }
            }
            $used[$u] = true;
            $answer += $dist[$u];
            for ($v = 0; $v < $n; $v++) {
                if (!$used[$v]) {
                    $d = abs($points[$u][0] - $points[$v][0]) + abs($points[$u][1] - $points[$v][1]);
                    if ($d < $dist[$v]) {
                        $dist[$v] = $d;
                    }
                }
            }
        }
        return $answer;
    }
}
