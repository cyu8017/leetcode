<?php
// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

class Solution {
    /**
     * @param Integer[][] $edges
     * @param Integer[] $patience
     * @return Integer
     */
    function networkBecomesIdle($edges, $patience) {
        $n = count($patience);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) { $g[$e[0]][] = $e[1]; $g[$e[1]][] = $e[0]; }
        $dist = array_fill(0, $n, -1);
        $q = [0];
        $dist[0] = 0;
        while ($q) {
            $u = array_shift($q);
            foreach ($g[$u] as $v) if ($dist[$v] === -1) { $dist[$v] = $dist[$u] + 1; $q[] = $v; }
        }
        $ans = 0;
        for ($i = 1; $i < $n; $i++) {
            $round = $dist[$i] * 2;
            $lastSend = intdiv($round - 1, $patience[$i]) * $patience[$i];
            $ans = max($ans, $lastSend + $round);
        }
        return $ans + 1;
    }
}
