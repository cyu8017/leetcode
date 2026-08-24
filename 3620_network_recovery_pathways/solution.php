<?php
// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

class Solution {
    function findMaxPathScore($edges, $online, $k) {
        $n = count($online);
        $g = array_fill(0, $n, []);
        $l = 2147483647;
        $r = 0;
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            if (!$online[$u] || !$online[$v]) continue;
            $g[$u][] = [$v, $w];
            $l = min($l, $w);
            $r = max($r, $w);
        }
        if ($l === 2147483647) return -1;
        $check = function($mid) use ($n, $g, $k) {
            $INF = 1073741823;
            $dist = array_fill(0, $n, $INF);
            $dist[0] = 0;
            $pq = [[0, 0]];
            while ($pq) {
                usort($pq, function($a, $b) { return $a[0] <=> $b[0]; });
                $cur = array_shift($pq);
                $d = $cur[0];
                $u = $cur[1];
                if ($d > $k) return false;
                if ($u === $n - 1) return true;
                if ($dist[$u] < $d) continue;
                foreach ($g[$u] as $e) {
                    $v = $e[0];
                    $w = $e[1];
                    if ($w < $mid) continue;
                    $nd = $d + $w;
                    if ($nd < $dist[$v]) {
                        $dist[$v] = $nd;
                        $pq[] = [$nd, $v];
                    }
                }
            }
            return false;
        };
        while ($l < $r) {
            $mid = ($l + $r + 1) >> 1;
            if ($check($mid)) $l = $mid;
            else $r = $mid - 1;
        }
        return $check($l) ? $l : -1;
    }
}
