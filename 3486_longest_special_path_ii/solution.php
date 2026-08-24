<?php
// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

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
        $dfs = null;
        $dfs = function($u, $p, $dist, &$pathVals, &$pathDist) use (&$dfs, &$g, $nums, &$bestLen, &$bestNodes) {
            $pathVals[] = $nums[$u];
            $pathDist[] = $dist;
            $freq = [];
            $dups = 0;
            $left = 0;
            for ($right = 0; $right < count($pathVals); $right++) {
                $v = $pathVals[$right];
                $freq[$v] = ($freq[$v] ?? 0) + 1;
                if ($freq[$v] === 2) $dups++;
                while ($dups > 1) {
                    $lv = $pathVals[$left];
                    if ($freq[$lv] === 2) $dups--;
                    $freq[$lv]--;
                    $left++;
                }
            }
            $length = $dist - $pathDist[$left];
            $nodes = count($pathVals) - $left;
            if ($length > $bestLen || ($length === $bestLen && $nodes < $bestNodes)) {
                $bestLen = $length;
                $bestNodes = $nodes;
            }
            foreach ($g[$u] as $e) {
                if ($e[0] === $p) continue;
                $dfs($e[0], $u, $dist + $e[1], $pathVals, $pathDist);
            }
            array_pop($pathVals);
            array_pop($pathDist);
        };
        $pv = [];
        $pd = [];
        $dfs(0, -1, 0, $pv, $pd);
        return [$bestLen, $bestNodes];
    }
}
