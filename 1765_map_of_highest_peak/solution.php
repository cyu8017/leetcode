<?php
// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

class Solution {
    /**
     * @param Integer[][] $isWater
     * @return Integer[][]
     */
    function highestPeak($isWater) {
        $m = count($isWater);
        $n = count($isWater[0]);
        $dist = array_fill(0, $m, array_fill(0, $n, -1));
        $queue = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($isWater[$i][$j] == 1) {
                    $dist[$i][$j] = 0;
                    $queue[] = [$i, $j];
                }
            }
        }
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $head = 0;
        while ($head < count($queue)) {
            [$i, $j] = $queue[$head++];
            foreach ($dirs as [$di, $dj]) {
                $x = $i + $di;
                $y = $j + $dj;
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n && $dist[$x][$y] === -1) {
                    $dist[$x][$y] = $dist[$i][$j] + 1;
                    $queue[] = [$x, $y];
                }
            }
        }
        return $dist;
    }
}
