<?php
// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution {
    function distanceLimitedPathsExist($n, $edgeList, $queries) {
        $parent = range(0, $n - 1);
        $find = function($x) use (&$find, &$parent) {
            while ($x != $parent[$x]) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $ans = array_fill(0, count($queries), false);
        usort($edgeList, function($a, $b) { return $a[2] - $b[2]; });
        $qi = [];
        foreach ($queries as $j => $q) {
            $qi[] = [$q[2], $q[0], $q[1], $j];
        }
        usort($qi, function($a, $b) { return $a[0] - $b[0]; });
        $i = 0;
        $m = count($edgeList);
        foreach ($qi as [$limit, $p, $q, $idx]) {
            while ($i < $m && $edgeList[$i][2] < $limit) {
                $a = $edgeList[$i][0];
                $b = $edgeList[$i][1];
                $parent[$find($a)] = $find($b);
                $i++;
            }
            $ans[$idx] = $find($p) === $find($q);
        }
        return $ans;
    }
}
