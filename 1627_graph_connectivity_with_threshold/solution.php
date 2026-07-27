<?php
// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $threshold
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function areConnected($n, $threshold, $queries) {
        $parent = range(0, $n);
        $find = function ($x) use (&$parent, &$find) {
            while ($x != $parent[$x]) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        for ($d = $threshold + 1; $d <= $n; $d++) {
            for ($x = 2 * $d; $x <= $n; $x += $d) {
                $a = $find($d);
                $b = $find($x);
                if ($a != $b) {
                    $parent[$b] = $a;
                }
            }
        }
        $ans = [];
        foreach ($queries as $q) {
            $ans[] = $find($q[0]) === $find($q[1]);
        }
        return $ans;
    }
}
