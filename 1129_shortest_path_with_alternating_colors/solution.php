<?php
// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $redEdges
     * @param Integer[][] $blueEdges
     * @return Integer[]
     */
    function shortestAlternatingPaths($n, $redEdges, $blueEdges) {
        $red = array_fill(0, $n, []);
        $blue = array_fill(0, $n, []);
        foreach ($redEdges as [$a, $b]) $red[$a][] = $b;
        foreach ($blueEdges as [$a, $b]) $blue[$a][] = $b;
        $ans = array_fill(0, $n, -1);
        $ans[0] = 0;
        $seen = [];
        $seen['0,0'] = true;
        $seen['0,1'] = true;
        $queue = [[0, -1, 0]];
        $head = 0;
        while ($head < count($queue)) {
            [$node, $lastColor, $dist] = $queue[$head++];
            if ($ans[$node] === -1) $ans[$node] = $dist;
            foreach ([0, 1] as $color) {
                if ($color === $lastColor) continue;
                $edges = $color === 0 ? $red : $blue;
                foreach ($edges[$node] as $nei) {
                    $key = "$nei,$color";
                    if (!isset($seen[$key])) {
                        $seen[$key] = true;
                        $queue[] = [$nei, $color, $dist + 1];
                    }
                }
            }
        }
        return $ans;
    }
}
