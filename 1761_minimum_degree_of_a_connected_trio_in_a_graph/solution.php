<?php
// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function minTrioDegree($n, $edges) {
        $adj = array_fill(0, $n, array_fill(0, $n, false));
        $degree = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $u = $e[0] - 1;
            $v = $e[1] - 1;
            $adj[$u][$v] = true;
            $adj[$v][$u] = true;
            $degree[$u]++;
            $degree[$v]++;
        }
        $best = PHP_INT_MAX;
        foreach ($edges as $e) {
            $u = $e[0] - 1;
            $v = $e[1] - 1;
            for ($k = 0; $k < $n; $k++) {
                if ($adj[$u][$k] && $adj[$v][$k]) {
                    $total = $degree[$u] + $degree[$v] + $degree[$k] - 6;
                    if ($total < $best) {
                        $best = $total;
                    }
                }
            }
        }
        return $best === PHP_INT_MAX ? -1 : $best;
    }
}
