<?php
// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

class Solution {
    function permute($n) {
        $ans = [];
        $used = array_fill(0, $n + 1, false);
        $cur = [];
        $dfs = null;
        $dfs = function() use (&$dfs, $n, &$ans, &$used, &$cur) {
            if (count($cur) === $n) {
                $ans[] = $cur;
                return;
            }
            for ($i = 1; $i <= $n; $i++) {
                if ($used[$i]) continue;
                if (count($cur) && ($cur[count($cur) - 1] % 2 === $i % 2)) continue;
                $used[$i] = true;
                $cur[] = $i;
                $dfs();
                array_pop($cur);
                $used[$i] = false;
            }
        };
        $dfs();
        return $ans;
    }
}
