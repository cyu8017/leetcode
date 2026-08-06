<?php
class Solution {
    function numOfMinutes($n, $headID, $manager, $informTime) {
        $children = array_fill(0, $n, []);
        foreach ($manager as $i => $p) {
            if ($p !== -1) $children[$p][] = $i;
        }
        $dfs = function($u) use (&$dfs, $children, $informTime) {
            $best = 0;
            foreach ($children[$u] as $v) $best = max($best, $dfs($v));
            return $informTime[$u] + $best;
        };
        return $dfs($headID);
    }
}
