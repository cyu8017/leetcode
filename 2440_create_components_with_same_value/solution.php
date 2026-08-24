<?php
// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

class Solution {
    function componentValue($nums, $edges) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $dfs = function ($u, $p, $target) use (&$dfs, &$g, $nums) {
            $sum = $nums[$u];
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $sub = $dfs($v, $u, $target);
                if ($sub < 0) return -1;
                $sum += $sub;
            }
            if ($sum > $target) return -1;
            if ($sum === $target) return 0;
            return $sum;
        };
        for ($parts = $n; $parts >= 1; $parts--) {
            if ($total % $parts !== 0) continue;
            $target = intdiv($total, $parts);
            if ($dfs(0, -1, $target) === 0) return $parts - 1;
        }
        return 0;
    }
}
