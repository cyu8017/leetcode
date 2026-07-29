<?php
// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $paths
     * @return Integer[]
     */
    function gardenNoAdj($n, $paths) {
        $graph = array_fill(0, $n + 1, []);
        foreach ($paths as $path) {
            $a = $path[0];
            $b = $path[1];
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $ans = array_fill(0, $n + 1, 0);
        for ($garden = 1; $garden <= $n; $garden++) {
            $used = [];
            foreach ($graph[$garden] as $nei) {
                $used[$ans[$nei]] = true;
            }
            for ($c = 1; $c <= 4; $c++) {
                if (!isset($used[$c])) {
                    $ans[$garden] = $c;
                    break;
                }
            }
        }
        return array_slice($ans, 1);
    }
}
