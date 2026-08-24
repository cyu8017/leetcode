<?php
// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution {
    function leftmostBuildingQueries($heights, $queries) {
        $qn = count($queries);
        $ans = array_fill(0, $qn, -1);
        $n = count($heights);
        $buckets = array_fill(0, $n, []);
        for ($qi = 0; $qi < $qn; $qi++) {
            $a = $queries[$qi][0];
            $b = $queries[$qi][1];
            if ($a > $b) { $t = $a; $a = $b; $b = $t; }
            if ($a === $b || $heights[$a] < $heights[$b]) {
                $ans[$qi] = $b;
                continue;
            }
            $buckets[$b][] = [$heights[$a], $qi];
        }
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            foreach ($buckets[$i] as $p) {
                $h = $p[0];
                $qi = $p[1];
                $lo = 0;
                $hi = count($st) - 1;
                $pos = -1;
                while ($lo <= $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($st[$mid][0] > $h) {
                        $pos = $st[$mid][1];
                        $lo = $mid + 1;
                    } else $hi = $mid - 1;
                }
                $ans[$qi] = $pos;
            }
            while (count($st) && $st[count($st) - 1][0] <= $heights[$i]) array_pop($st);
            $st[] = [$heights[$i], $i];
        }
        return $ans;
    }
}
