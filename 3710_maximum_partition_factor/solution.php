<?php
// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

class Solution {
    function maxPartitionFactor($points) {
        $n = count($points);
        if ($n === 2) return 0;
        $dist = function($i, $j) use ($points) {
            return abs($points[$i][0] - $points[$j][0]) + abs($points[$i][1] - $points[$j][1]);
        };
        $ok = function($d) use ($n, $dist) {
            $g = array_fill(0, $n, []);
            for ($i = 0; $i < $n; $i++) {
                for ($j = $i + 1; $j < $n; $j++) {
                    if ($dist($i, $j) < $d) {
                        $g[$i][] = $j;
                        $g[$j][] = $i;
                    }
                }
            }
            $color = array_fill(0, $n, -1);
            for ($i = 0; $i < $n; $i++) {
                if ($color[$i] !== -1) continue;
                $q = [$i];
                $color[$i] = 0;
                while ($q) {
                    $u = array_shift($q);
                    foreach ($g[$u] as $v) {
                        if ($color[$v] === -1) {
                            $color[$v] = $color[$u] ^ 1;
                            $q[] = $v;
                        } else if ($color[$v] === $color[$u]) return false;
                    }
                }
            }
            return true;
        };
        $lo = 0;
        $hi = 0;
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                $hi = max($hi, $dist($i, $j));
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
