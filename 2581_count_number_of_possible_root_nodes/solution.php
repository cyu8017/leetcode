<?php
// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

class Solution {
    function rootCount($edges, $guesses, $k) {
        $n = count($edges) + 1;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $guessSet = [];
        foreach ($guesses as $gu) $guessSet[$gu[0] . ',' . $gu[1]] = true;
        $dfs1 = function($u, $p) use (&$dfs1, &$g, &$guessSet) {
            $cnt = 0;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                if (isset($guessSet[$u . ',' . $v])) $cnt++;
                $cnt += $dfs1($v, $u);
            }
            return $cnt;
        };
        $ans = 0;
        $dfs2 = function($u, $p, $cur) use (&$dfs2, &$g, &$guessSet, $k, &$ans) {
            if ($cur >= $k) $ans++;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $nxt = $cur;
                if (isset($guessSet[$u . ',' . $v])) $nxt--;
                if (isset($guessSet[$v . ',' . $u])) $nxt++;
                $dfs2($v, $u, $nxt);
            }
        };
        $baseCnt = $dfs1(0, -1);
        $dfs2(0, -1, $baseCnt);
        return $ans;
    }
}
