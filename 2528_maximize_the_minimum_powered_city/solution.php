<?php
// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution {
    function maxPower($stations, $r, $k) {
        $n = count($stations);
        $diff = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $L = max(0, $i - $r);
            $R = min($n - 1, $i + $r);
            $diff[$L] += $stations[$i];
            $diff[$R + 1] -= $stations[$i];
        }
        $power = array_fill(0, $n, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $power[$i] = $cur;
        }
        $lo = 0;
        $hi = $k;
        foreach ($power as $p) if ($p > $hi) $hi = $p;
        $hi += $k;
        $ok = function($x) use ($n, $r, $k, $power) {
            $extra = array_fill(0, $n + 1, 0);
            $have = 0;
            $used = 0;
            for ($i = 0; $i < $n; $i++) {
                $have += $extra[$i];
                $need = $x - ($power[$i] + $have);
                if ($need > 0) {
                    $used += $need;
                    if ($used > $k) return false;
                    $have += $need;
                    $end = $i + 2 * $r;
                    if ($end + 1 <= $n) $extra[$end + 1] -= $need;
                }
            }
            return true;
        };
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
