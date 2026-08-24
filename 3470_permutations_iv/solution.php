<?php
// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

class Solution {
    function permute($n, $k) {
        $fact = array_fill(0, $n + 1, 1);
        $cap = 10 ** 18 + 1;
        for ($i = 1; $i <= $n; $i++) {
            $fact[$i] = $fact[$i - 1] * $i;
            if ($fact[$i] > $cap) $fact[$i] = $cap;
        }
        $used = array_fill(0, $n + 1, false);
        $ans = [];
        $kk = $k;
        $dfs = null;
        $dfs = function($pos) use (&$dfs, $n, &$kk, $fact, &$used, &$ans) {
            if ($pos === $n) return true;
            for ($x = 1; $x <= $n; $x++) {
                if ($used[$x]) continue;
                if ($pos > 0 && ($ans[$pos - 1] % 2 === $x % 2)) continue;
                $rem = $n - $pos - 1;
                $cnt = $fact[$rem];
                if ($cnt >= $kk) {
                    $used[$x] = true;
                    $ans[] = $x;
                    if ($dfs($pos + 1)) return true;
                    array_pop($ans);
                    $used[$x] = false;
                } else {
                    $kk -= $cnt;
                }
            }
            return false;
        };
        if (!$dfs(0)) return [];
        return $ans;
    }
}
