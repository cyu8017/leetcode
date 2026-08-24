<?php
// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

class Solution {
    function minMaxWeight($n, $edges, $threshold) {
        $ok = function($mid) use ($n, $edges) {
            $g = [];
            for ($i = 0; $i < $n; $i++) $g[$i] = [];
            foreach ($edges as $e) {
                if ($e[2] <= $mid) $g[$e[1]][] = $e[0];
            }
            $vis = array_fill(0, $n, false);
            $q = [0];
            $vis[0] = true;
            $cnt = 1;
            while (count($q)) {
                $u = array_shift($q);
                foreach ($g[$u] as $v) {
                    if (!$vis[$v]) {
                        $vis[$v] = true;
                        $cnt++;
                        $q[] = $v;
                    }
                }
            }
            return $cnt === $n;
        };
        $lo = 1;
        $hi = 1000001;
        $ans = -1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) {
                $ans = $mid;
                $hi = $mid;
            } else $lo = $mid + 1;
        }
        return $ans;
    }
}
