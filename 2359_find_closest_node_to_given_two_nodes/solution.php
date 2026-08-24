<?php
// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

class Solution {
    function closestMeetingNode($edges, $node1, $node2) {
        $d1 = $this->dist($edges, $node1);
        $d2 = $this->dist($edges, $node2);
        $n = count($edges);
        $ans = -1;
        $best = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            if ($d1[$i] === -1 || $d2[$i] === -1) continue;
            $mx = max($d1[$i], $d2[$i]);
            if ($mx < $best) { $best = $mx; $ans = $i; }
        }
        return $ans;
    }

    private function dist($edges, $start) {
        $n = count($edges);
        $d = array_fill(0, $n, -1);
        $cur = $start;
        $step = 0;
        while ($cur !== -1 && $d[$cur] === -1) {
            $d[$cur] = $step;
            $cur = $edges[$cur];
            $step++;
        }
        return $d;
    }
}
