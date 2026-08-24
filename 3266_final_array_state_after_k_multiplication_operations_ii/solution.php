<?php
// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

class Solution {
    function getFinalState($nums, $k, $multiplier) {
        $mod = 1000000007;
        if ($multiplier === 1) return $nums;
        $n = count($nums);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $maxV = 0;
        for ($i = 0; $i < $n; $i++) {
            $pq->insert($i, [-$nums[$i], -$i]);
            if ($nums[$i] > $maxV) $maxV = $nums[$i];
        }
        while ($k > 0 && !$pq->isEmpty()) {
            $item = $pq->extract();
            $i = $item['data'];
            $v = $nums[$i];
            if ($multiplier !== 0 && $v > intdiv($maxV, $multiplier) && $k >= $n) {
                $pq->insert($i, [-$v, -$i]);
                break;
            }
            $nv = $v * $multiplier;
            $nums[$i] = $nv;
            if ($nv > $maxV) $maxV = $nv;
            $pq->insert($i, [-$nv, -$i]);
            $k--;
        }
        if ($k > 0) {
            $full = intdiv($k, $n);
            $rem = $k % $n;
            $powFull = $this->modPow($multiplier, $full, $mod);
            for ($i = 0; $i < $n; $i++) $nums[$i] = (int)(($nums[$i] % $mod) * $powFull % $mod);
            $hh = new SplPriorityQueue();
            $hh->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
            for ($i = 0; $i < $n; $i++) $hh->insert($i, [-$nums[$i], -$i]);
            for ($t = 0; $t < $rem; $t++) {
                $item = $hh->extract();
                $i = $item['data'];
                $v = (int)(($nums[$i] % $mod) * ($multiplier % $mod) % $mod);
                $nums[$i] = $v;
                $hh->insert($i, [-$v, -$i]);
            }
            for ($i = 0; $i < $n; $i++) $nums[$i] %= $mod;
        } else {
            for ($i = 0; $i < $n; $i++) $nums[$i] %= $mod;
        }
        return $nums;
    }

    private function modPow($a, $e, $mod) {
        $r = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $r = (int)(($r * $a) % $mod);
            $a = (int)(($a * $a) % $mod);
            $e >>= 1;
        }
        return $r;
    }
}
