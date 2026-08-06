<?php

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param String $labels
     * @return Integer[]
     */
    function countSubTrees($n, $edges, $labels) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $graph[$edge[0]][] = $edge[1];
            $graph[$edge[1]][] = $edge[0];
        }
        $answer = array_fill(0, $n, 0);
        $dfs = function ($node, $parent) use (&$dfs, &$graph, &$labels, &$answer) {
            $counts = array_fill(0, 26, 0);
            $index = ord($labels[$node]) - 97;
            $counts[$index] = 1;
            foreach ($graph[$node] as $neighbor) {
                if ($neighbor !== $parent) {
                    $child = $dfs($neighbor, $node);
                    for ($i = 0; $i < 26; $i++) {
                        $counts[$i] += $child[$i];
                    }
                }
            }
            $answer[$node] = $counts[$index];
            return $counts;
        };
        $dfs(0, -1);
        return $answer;
    }
}
