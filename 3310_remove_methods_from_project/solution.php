<?php
// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

class Solution {
    function remainingMethods($n, $k, $invocations) {
        $g = array_fill(0, $n, []);
        foreach ($invocations as $e) $g[$e[0]][] = $e[1];
        $sus = array_fill(0, $n, false);
        $this->dfs($k, $g, $sus);
        foreach ($invocations as $e) {
            if (!$sus[$e[0]] && $sus[$e[1]]) {
                $ans = [];
                for ($i = 0; $i < $n; $i++) $ans[] = $i;
                return $ans;
            }
        }
        $ans = [];
        for ($i = 0; $i < $n; $i++) if (!$sus[$i]) $ans[] = $i;
        return $ans;
    }

    function dfs($u, $g, &$sus) {
        if ($sus[$u]) return;
        $sus[$u] = true;
        foreach ($g[$u] as $v) $this->dfs($v, $g, $sus);
    }
}
