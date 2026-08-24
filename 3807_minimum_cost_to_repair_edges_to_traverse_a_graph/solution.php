<?php
// LeetCode 3807 - Minimum Cost to Repair Edges to Traverse a Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

class Solution {
    function minCost($n, $edges, $k) {
        usort($edges, function($a, $b) { return $a[2] <=> $b[2]; });
        $m = count($edges);
        if ($m === 0) return -1;
        $check = function($idx) use ($n, $edges, $k) {
            $g = array_fill(0, $n, []);
            for ($i = 0; $i <= $idx; $i++) {
                $g[$edges[$i][0]][] = $edges[$i][1];
                $g[$edges[$i][1]][] = $edges[$i][0];
            }
            $q = [0];
            $vis = array_fill(0, $n, false);
            $vis[0] = true;
            $dist = 0;
            while (count($q)) {
                $nq = [];
                foreach ($q as $u) {
                    if ($u === $n - 1) return $dist <= $k;
                    foreach ($g[$u] as $v) {
                        if (!$vis[$v]) {
                            $vis[$v] = true;
                            $nq[] = $v;
                        }
                    }
                }
                $q = $nq;
                $dist++;
            }
            return false;
        };
        $l = 0;
        $r = $m - 1;
        while ($l < $r) {
            $mid = ($l + $r) >> 1;
            if ($check($mid)) $r = $mid;
            else $l = $mid + 1;
        }
        if ($check($l)) return $edges[$l][2];
        return -1;
    }
}
