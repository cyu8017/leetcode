<?php
// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

class Solution {
    function shortestDistanceAfterQueries($n, $queries) {
        $nxt = [];
        for ($i = 0; $i < $n - 1; $i++) $nxt[$i] = $i + 1;
        $cnt = $n - 1;
        $ans = [];
        foreach ($queries as $q) {
            $u = $q[0];
            $v = $q[1];
            if (isset($nxt[$u]) && $nxt[$u] > 0 && $nxt[$u] < $v) {
                $i = $nxt[$u];
                while ($i < $v) {
                    $cnt--;
                    $ni = $nxt[$i];
                    $nxt[$i] = 0;
                    $i = $ni;
                }
                $nxt[$u] = $v;
            }
            $ans[] = $cnt;
        }
        return $ans;
    }
}
