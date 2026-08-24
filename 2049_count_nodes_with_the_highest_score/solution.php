<?php
// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

class Solution {
    /**
     * @param Integer[] $parents
     * @return Integer
     */
    function countHighestScoreNodes($parents) {
        $n = count($parents);
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $children[$parents[$i]][] = $i;
        $size = array_fill(0, $n, 0);
        $dfs = null;
        $dfs = function ($u) use (&$dfs, &$size, &$children) {
            $size[$u] = 1;
            foreach ($children[$u] as $v) $size[$u] += $dfs($v);
            return $size[$u];
        };
        $dfs(0);
        $best = 0;
        $ans = 0;
        for ($u = 0; $u < $n; $u++) {
            $score = 1;
            foreach ($children[$u] as $v) $score *= $size[$v];
            $up = $n - $size[$u];
            if ($up > 0) $score *= $up;
            if ($score > $best) { $best = $score; $ans = 1; }
            else if ($score === $best) $ans++;
        }
        return $ans;
    }
}
