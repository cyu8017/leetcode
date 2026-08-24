<?php
// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

class Solution {
    function minThreshold($n, $edges, $source, $target, $k) {
        if ($source === $target) return 0;
        $g = array_fill(0, $n, []);
        $maxWeight = 0;
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
            $maxWeight = max($maxWeight, $e[2]);
        }
        if (!$this->can($n, $g, $source, $target, $k, $maxWeight)) return -1;
        $lo = 0;
        $hi = $maxWeight;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($this->can($n, $g, $source, $target, $k, $mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }

    private function can($n, $g, $source, $target, $k, $threshold) {
        $inf = 1000000000;
        $dist = array_fill(0, $n, $inf);
        $dist[$source] = 0;
        $dq = [$source];
        while (count($dq) > 0) {
            $u = array_shift($dq);
            foreach ($g[$u] as $e) {
                $to = $e[0];
                $weight = $e[1];
                $cost = $weight > $threshold ? 1 : 0;
                if ($dist[$u] + $cost >= $dist[$to] || $dist[$u] + $cost > $k) continue;
                $dist[$to] = $dist[$u] + $cost;
                if ($cost === 0) array_unshift($dq, $to);
                else $dq[] = $to;
            }
        }
        return $dist[$target] <= $k;
    }
}
