<?php
// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function sumOfDistancesInTree($n, $edges) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = $e[1];
            $graph[$e[1]][] = $e[0];
        }
        $count = array_fill(0, $n, 1);
        $ans = array_fill(0, $n, 0);
        $post = function($node, $parent) use (&$post, $graph, &$count, &$ans) {
            foreach ($graph[$node] as $child) {
                if ($child === $parent) continue;
                $post($child, $node);
                $count[$node] += $count[$child];
                $ans[$node] += $ans[$child] + $count[$child];
            }
        };
        $reroot = function($node, $parent) use (&$reroot, $graph, $count, &$ans, $n) {
            foreach ($graph[$node] as $child) {
                if ($child === $parent) continue;
                $ans[$child] = $ans[$node] - $count[$child] + ($n - $count[$child]);
                $reroot($child, $node);
            }
        };
        $post(0, -1);
        $reroot(0, -1);
        return $ans;
    }
}
