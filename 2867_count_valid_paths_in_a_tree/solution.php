<?php
// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

class Solution {
    function countPaths($n, $edges) {
        $isPrime = array_fill(0, $n + 1, true);
        $isPrime[0] = false;
        $isPrime[1] = false;
        for ($i = 2; $i * $i <= $n; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $n; $j += $i) $isPrime[$j] = false;
            }
        }
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $dfs = function($u, $p) use (&$dfs, &$g, &$isPrime) {
            if ($isPrime[$u]) return 0;
            $sz = 1;
            foreach ($g[$u] as $v) if ($v !== $p) $sz += $dfs($v, $u);
            return $sz;
        };
        $ans = 0;
        for ($u = 1; $u <= $n; $u++) {
            if (!$isPrime[$u]) continue;
            $total = 0;
            foreach ($g[$u] as $v) {
                $c = $dfs($v, $u);
                $ans += $c;
                $ans += $total * $c;
                $total += $c;
            }
        }
        return $ans;
    }
}
