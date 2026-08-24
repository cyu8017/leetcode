<?php
// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

class Solution {
    function minTime($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) $g[$e[0]][] = [$e[1], $e[2], $e[3]];
        $Inf = 1e18;
        $dist = array_fill(0, $n, $Inf);
        $dist[0] = 0;
        $pq = [[0, 0]];
        $push = function($t, $u) use (&$pq) {
            $lo = 0;
            $hi = count($pq);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($pq[$mid][0] < $t) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($pq, $lo, 0, [[$t, $u]]);
        };
        while (count($pq)) {
            $cur = array_shift($pq);
            $t = $cur[0];
            $u = $cur[1];
            if ($t !== $dist[$u]) continue;
            if ($u === $n - 1) return $t;
            foreach ($g[$u] as $e) {
                $nt = $t;
                if ($nt > $e[2]) continue;
                if ($nt < $e[1]) $nt = $e[1];
                $nt += 1;
                if ($nt < $dist[$e[0]]) {
                    $dist[$e[0]] = $nt;
                    $push($nt, $e[0]);
                }
            }
        }
        return $dist[$n - 1] === $Inf ? -1 : $dist[$n - 1];
    }
}
