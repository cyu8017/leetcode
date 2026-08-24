<?php
// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

class Solution {
    function maxLen($n, $edges, $label) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $pack = function($a, $b) {
            return $a . ',' . $b;
        };
        $expandPal = function($l, $r) use ($g, $label, $pack) {
            $vis = [];
            $q = [];
            $len0 = $l !== $r ? 2 : 1;
            $q[] = [$l, $r, $len0];
            $best = $len0;
            $vis[$pack(min($l, $r), max($l, $r))] = true;
            while ($q) {
                $cur = array_shift($q);
                foreach ($g[$cur[0]] as $a) {
                    foreach ($g[$cur[1]] as $b) {
                        if ($a === $b || $label[$a] !== $label[$b]) continue;
                        $p = $pack(min($a, $b), max($a, $b));
                        if (isset($vis[$p])) continue;
                        $vis[$p] = true;
                        $nl = $cur[2] + 2;
                        $best = max($best, $nl);
                        $q[] = [$a, $b, $nl];
                    }
                }
            }
            return $best;
        };
        $ans = 1;
        for ($i = 0; $i < $n; $i++) {
            $ans = max($ans, $expandPal($i, $i));
            foreach ($g[$i] as $j) {
                if ($i < $j && $label[$i] === $label[$j])
                    $ans = max($ans, $expandPal($i, $j));
            }
        }
        return $ans;
    }
}
