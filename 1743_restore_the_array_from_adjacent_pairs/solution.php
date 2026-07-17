<?php
// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution {
    /**
     * @param Integer[][] $adjacentPairs
     * @return Integer[]
     */
    function restoreArray($adjacentPairs) {
        $graph = [];
        foreach ($adjacentPairs as [$a, $b]) {
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $start = null;
        foreach ($graph as $node => $neighbors) {
            if (count($neighbors) === 1) {
                $start = $node;
                break;
            }
        }
        $ans = [$start];
        $prev = null;
        $n = count($graph);
        while (count($ans) < $n) {
            $cur = $ans[count($ans) - 1];
            $neighbors = $graph[$cur];
            $nxt = ($prev === null || $neighbors[0] !== $prev) ? $neighbors[0] : $neighbors[1];
            $ans[] = $nxt;
            $prev = $cur;
        }
        return $ans;
    }
}
