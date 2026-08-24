<?php
// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

class Solution {
    function minTime($n, $k, $m, $time, $mul) {
        if ($k === 1 && $n > 1) return -1.0;
        $full = (1 << $n) - 1;
        $INF = 1e18;
        $best = [];
        for ($mask = 0; $mask <= $full; $mask++) {
            $best[$mask] = [];
            for ($boat = 0; $boat < 2; $boat++)
                $best[$mask][$boat] = array_fill(0, $m, $INF);
        }
        $best[0][0][0] = 0.0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0.0, 0, 0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $t = $cur[0];
            $mask = $cur[1];
            $boat = $cur[2];
            $stage = $cur[3];
            if ($t > $best[$mask][$boat][$stage] + 1e-9) continue;
            if ($mask === $full && $boat === 1) return $t;
            if ($boat === 0) {
                $camp = $full ^ $mask;
                for ($sub = $camp; $sub > 0; $sub = ($sub - 1) & $camp) {
                    $cnt = 0;
                    $mx = 0;
                    for ($i = 0; $i < $n; $i++) {
                        if (($sub >> $i) & 1) {
                            $cnt++;
                            if ($time[$i] > $mx) $mx = $time[$i];
                        }
                    }
                    if ($cnt === 0 || $cnt > $k) continue;
                    $d = $mx * $mul[$stage];
                    $ns = ($stage + (int)floor($d)) % $m;
                    $nm = $mask | $sub;
                    $nt = $t + $d;
                    if ($nt < $best[$nm][1][$ns] - 1e-12) {
                        $best[$nm][1][$ns] = $nt;
                        $pq->insert([$nt, $nm, 1, $ns], -$nt);
                    }
                }
            } else {
                if ($mask === $full) continue;
                for ($i = 0; $i < $n; $i++) {
                    if ((($mask >> $i) & 1) === 0) continue;
                    $d = $time[$i] * $mul[$stage];
                    $ns = ($stage + (int)floor($d)) % $m;
                    $nm = $mask ^ (1 << $i);
                    $nt = $t + $d;
                    if ($nt < $best[$nm][0][$ns] - 1e-12) {
                        $best[$nm][0][$ns] = $nt;
                        $pq->insert([$nt, $nm, 0, $ns], -$nt);
                    }
                }
            }
        }
        return -1.0;
    }
}
