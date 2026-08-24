<?php
// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

class Solution {
    function longestSpecialPath($edges, $nums) {
        $n = count($nums);
        $g = [];
        for ($i = 0; $i < $n; $i++) $g[$i] = [];
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $bestLen = 0;
        $bestNodes = 1;
        $last = [];
        $path = [];
        $dfs = null;
        $dfs = function($u, $p, $dist, $left) use (&$dfs, &$g, &$nums, &$bestLen, &$bestNodes, &$last, &$path) {
            $seen = isset($last[$nums[$u]]);
            $prevPos = $seen ? $last[$nums[$u]] : -1;
            $last[$nums[$u]] = count($path);
            $newLeft = $left;
            if ($seen && $prevPos >= $left) $newLeft = $prevPos + 1;
            $path[] = $dist;
            $length = $dist - $path[$newLeft];
            $nodes = count($path) - $newLeft;
            if ($length > $bestLen || ($length === $bestLen && $nodes < $bestNodes)) {
                $bestLen = $length;
                $bestNodes = $nodes;
            }
            foreach ($g[$u] as $e) {
                if ($e[0] === $p) continue;
                $dfs($e[0], $u, $dist + $e[1], $newLeft);
            }
            array_pop($path);
            if ($seen) $last[$nums[$u]] = $prevPos;
            else unset($last[$nums[$u]]);
        };
        $dfs(0, -1, 0, 0);
        return [$bestLen, $bestNodes];
    }
}
