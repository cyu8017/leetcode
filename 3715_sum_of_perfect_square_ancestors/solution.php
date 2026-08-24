<?php
// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

class Solution {
    function sumOfAncestors($n, $edges, $nums) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = $e[1];
            $graph[$e[1]][] = $e[0];
        }
        $kernel = function($x) {
            $res = 1;
            for ($p = 2; $p * $p <= $x; $p++) {
                $cnt = 0;
                while ($x % $p === 0) {
                    $x = intdiv($x, $p);
                    $cnt++;
                }
                if ($cnt % 2 === 1) $res *= $p;
            }
            if ($x > 1) $res *= $x;
            return $res;
        };
        $ks = [];
        for ($i = 0; $i < $n; $i++) $ks[$i] = $kernel($nums[$i]);
        $freq = [];
        $ans = 0;
        $dfs = function($u, $p) use (&$dfs, &$freq, &$ans, $ks, $graph) {
            $ans += isset($freq[$ks[$u]]) ? $freq[$ks[$u]] : 0;
            if (!isset($freq[$ks[$u]])) $freq[$ks[$u]] = 0;
            $freq[$ks[$u]]++;
            foreach ($graph[$u] as $v) if ($v !== $p) $dfs($v, $u);
            $freq[$ks[$u]]--;
        };
        $dfs(0, -1);
        return $ans;
    }
}
