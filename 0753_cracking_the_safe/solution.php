<?php
// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

class Solution {
    function crackSafe($n, $k) {
        $seen = [];
        $path = [];
        $start = '';
        for ($i = 0; $i < $n - 1; $i++) $start .= '0';
        $dfs = function ($node) use (&$dfs, &$seen, &$path, $k) {
            for ($d = 0; $d < $k; $d++) {
                $digit = (string)$d;
                $edge = $node . $digit;
                if (!isset($seen[$edge])) {
                    $seen[$edge] = true;
                    $dfs(substr($edge, 1));
                    $path[] = $digit;
                }
            }
        };
        $dfs($start);
        return implode('', $path) . $start;
    }
}
