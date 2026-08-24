<?php
// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

class Solution {
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        $pairs = [];
        for ($i = 0; $i < $n; $i++) $pairs[] = [$nums[$i], $i];
        usort($pairs, function($a, $b) { return $a[0] <=> $b[0]; });
        $m = 20;
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $m, 0);
        $r = $n - 1;
        for ($l = $n - 1; $l >= 0; $l--) {
            while ($pairs[$r][0] - $pairs[$l][0] > $maxDiff) $r--;
            $i = $pairs[$l][1];
            $j = $pairs[$r][1];
            $f[$i][0] = $j;
            for ($k = 1; $k < $m; $k++) $f[$i][$k] = $f[$f[$i][$k - 1]][$k - 1];
        }
        $ans = [];
        foreach ($queries as $q) {
            $i = $q[0];
            $j = $q[1];
            if ($nums[$i] > $nums[$j]) { $tmp = $i; $i = $j; $j = $tmp; }
            if ($i === $j) { $ans[] = 0; continue; }
            if ($nums[$i] === $nums[$j]) { $ans[] = 1; continue; }
            $d = 0;
            for ($k = $m - 1; $k >= 0; $k--) {
                if ($nums[$f[$i][$k]] < $nums[$j]) {
                    $d |= 1 << $k;
                    $i = $f[$i][$k];
                }
            }
            if ($nums[$f[$i][0]] < $nums[$j]) $ans[] = -1;
            else $ans[] = $d + 1;
        }
        return $ans;
    }
}
