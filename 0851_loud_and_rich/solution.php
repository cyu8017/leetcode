<?php
// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

class Solution {
    /**
     * @param Integer[][] $richer
     * @param Integer[] $quiet
     * @return Integer[]
     */
    function loudAndRich($richer, $quiet) {
        $n = count($quiet);
        $graph = array_fill(0, $n, []);
        foreach ($richer as $e) $graph[$e[1]][] = $e[0];
        $ans = array_fill(0, $n, -1);
        $dfs = function($person) use (&$dfs, $graph, $quiet, &$ans) {
            if ($ans[$person] !== -1) return $ans[$person];
            $best = $person;
            foreach ($graph[$person] as $richerPerson) {
                $cand = $dfs($richerPerson);
                if ($quiet[$cand] < $quiet[$best]) $best = $cand;
            }
            $ans[$person] = $best;
            return $best;
        };
        for ($i = 0; $i < $n; $i++) $dfs($i);
        return $ans;
    }
}
