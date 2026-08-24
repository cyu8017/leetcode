<?php
// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function findMinHeightTrees($n, $edges) {
        if ($n <= 2) {
            return range(0, $n - 1);
        }

        $graph = array_fill(0, $n, []);
        $degree = array_fill(0, $n, 0);
        foreach ($edges as $edge) {
            $left = $edge[0];
            $right = $edge[1];
            $graph[$left][] = $right;
            $graph[$right][] = $left;
            $degree[$left]++;
            $degree[$right]++;
        }

        $leaves = [];
        for ($node = 0; $node < $n; $node++) {
            if ($degree[$node] === 1) {
                $leaves[] = $node;
            }
        }

        $remaining = $n;
        while ($remaining > 2) {
            $remaining -= count($leaves);
            $newLeaves = [];
            foreach ($leaves as $leaf) {
                foreach ($graph[$leaf] as $neighbor) {
                    $degree[$neighbor]--;
                    if ($degree[$neighbor] === 1) {
                        $newLeaves[] = $neighbor;
                    }
                }
            }
            $leaves = $newLeaves;
        }
        return $leaves;
    }
}
