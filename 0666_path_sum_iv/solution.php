<?php
// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

class Solution {
    function pathSum($nums) {
        $tree = [];
        $total = 0;
        foreach ($nums as $num) {
            $tree[intdiv($num, 100) . "," . (intdiv($num, 10) % 10)] = $num % 10;
        }
        $dfs = function($depth, $pos, $path) use (&$dfs, &$tree, &$total) {
            $k = $depth . "," . $pos;
            if (!isset($tree[$k])) return;
            $path += $tree[$k];
            $left = ($depth + 1) . "," . ($pos * 2 - 1);
            $right = ($depth + 1) . "," . ($pos * 2);
            if (!isset($tree[$left]) && !isset($tree[$right])) {
                $total += $path;
                return;
            }
            $dfs($depth + 1, $pos * 2 - 1, $path);
            $dfs($depth + 1, $pos * 2, $path);
        };
        $dfs(1, 1, 0);
        return $total;
    }
}
