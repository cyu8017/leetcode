<?php
// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $roads
     * @return Integer
     */
    function maximalNetworkRank($n, $roads) {
        $degree = array_fill(0, $n, 0);
        $edges = [];
        foreach ($roads as $r) {
            $a = $r[0];
            $b = $r[1];
            $degree[$a]++;
            $degree[$b]++;
            $key = min($a, $b) . "," . max($a, $b);
            $edges[$key] = true;
        }
        $ans = 0;
        for ($a = 0; $a < $n; $a++) {
            for ($b = $a + 1; $b < $n; $b++) {
                $key = $a . "," . $b;
                $ans = max($ans, $degree[$a] + $degree[$b] - (isset($edges[$key]) ? 1 : 0));
            }
        }
        return $ans;
    }
}
