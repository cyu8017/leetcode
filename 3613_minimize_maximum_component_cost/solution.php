<?php
// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

class Solution {
    function minCost($n, $edges, $k) {
        $p = range(0, $n - 1);
        $find = function($x) use (&$p, &$find) {
            return $p[$x] === $x ? $x : ($p[$x] = $find($p[$x]));
        };
        if ($k === $n) return 0;
        usort($edges, function($a, $b) { return $a[2] <=> $b[2]; });
        $cnt = $n;
        foreach ($edges as $e) {
            $pu = $find($e[0]);
            $pv = $find($e[1]);
            if ($pu !== $pv) {
                $p[$pu] = $pv;
                if (--$cnt <= $k) return $e[2];
            }
        }
        return 0;
    }
}
