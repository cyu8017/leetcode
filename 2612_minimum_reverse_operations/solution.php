<?php
// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

class Solution {
    function minReverseOperations($n, $p, $banned, $k) {
        $ban = [];
        foreach ($banned as $x) $ban[$x] = true;
        $ans = array_fill(0, $n, -1);
        $ans[$p] = 0;
        $q = [[$p, 0]];
        while ($q) {
            $cur = array_shift($q);
            $i = $cur[0];
            $d = $cur[1];
            $lo = $i - ($k - 1);
            if ($lo < 0) $lo = 0;
            $hi = $i;
            if ($hi > $n - $k) $hi = $n - $k;
            for ($L = $lo; $L <= $hi; $L++) {
                $R = $L + $k - 1;
                $ni = $L + $R - $i;
                if ($ni < 0 || $ni >= $n || isset($ban[$ni]) || $ans[$ni] !== -1) continue;
                $ans[$ni] = $d + 1;
                $q[] = [$ni, $d + 1];
            }
        }
        return $ans;
    }
}
