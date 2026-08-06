<?php
// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

class Solution {
    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function treeDiameter($edges) {
        if (empty($edges)) return 0;
        $graph = [];
        foreach ($edges as [$a, $b]) {
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $farthest = function ($start) use ($graph) {
            $queue = [[$start, 0]];
            $seen = [$start => true];
            $head = 0;
            $last = [$start, 0];
            while ($head < count($queue)) {
                $last = $queue[$head++];
                foreach ($graph[$last[0]] ?? [] as $v) {
                    if (!isset($seen[$v])) {
                        $seen[$v] = true;
                        $queue[] = [$v, $last[1] + 1];
                    }
                }
            }
            return $last;
        };
        [$endpoint] = $farthest($edges[0][0]);
        return $farthest($endpoint)[1];
    }
}
