<?php
// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

class Solution {
    /**
     * @param Integer[][] $pairs
     * @return Integer
     */
    function checkWays($pairs) {
        $graph = [];
        foreach ($pairs as [$a, $b]) {
            $graph[$a][$b] = true;
            $graph[$b][$a] = true;
        }
        $nodes = array_keys($graph);
        $n = count($nodes);
        $root = null;
        foreach ($nodes as $node) {
            if (count($graph[$node]) === $n - 1) {
                $root = $node;
                break;
            }
        }
        if ($root === null) {
            return 0;
        }
        $ans = 1;
        foreach ($nodes as $node) {
            if ($node === $root) {
                continue;
            }
            $parent = null;
            $parentDegree = $n + 1;
            foreach (array_keys($graph[$node]) as $nei) {
                $neiDegree = count($graph[$nei]);
                if ($neiDegree >= count($graph[$node]) && $neiDegree < $parentDegree) {
                    $parent = $nei;
                    $parentDegree = $neiDegree;
                }
            }
            if ($parent === null) {
                return 0;
            }
            foreach (array_keys($graph[$node]) as $nei) {
                if ($nei !== $parent && !isset($graph[$parent][$nei])) {
                    return 0;
                }
            }
            if (count($graph[$parent]) === count($graph[$node])) {
                $ans = 2;
            }
        }
        return $ans;
    }
}
