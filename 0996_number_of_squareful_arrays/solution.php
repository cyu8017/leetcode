<?php
// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numSquarefulPerms($nums) {
        $count = [];
        foreach ($nums as $x) $count[$x] = ($count[$x] ?? 0) + 1;
        $graph = [];
        foreach ($count as $a => $_) $graph[$a] = [];
        foreach ($count as $a => $_) {
            foreach ($count as $b => $__) {
                $s = $a + $b;
                $r = (int)round(sqrt($s));
                if ($r * $r === $s) $graph[$a][] = $b;
            }
        }
        $ans = 0;
        $dfs = null;
        $dfs = function ($x, $remain) use (&$dfs, &$count, &$graph, &$ans) {
            if ($remain === 0) { $ans++; return; }
            foreach ($graph[$x] as $y) {
                if (($count[$y] ?? 0) > 0) {
                    $count[$y]--;
                    $dfs($y, $remain - 1);
                    $count[$y]++;
                }
            }
        };
        foreach (array_keys($count) as $x) {
            $count[$x]--;
            $dfs($x, count($nums) - 1);
            $count[$x]++;
        }
        return $ans;
    }
}
