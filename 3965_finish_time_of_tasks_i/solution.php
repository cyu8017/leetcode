<?php
// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

class Solution {
    private $baseTime;
    private $g;

    function finishTime($n, $edges, $baseTime) {
        $this->baseTime = $baseTime;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) $this->g[$e[0]][] = $e[1];
        return $this->dfs(0);
    }

    private function dfs($i) {
        if (count($this->g[$i]) === 0) return $this->baseTime[$i];
        $INF = 1 << 62;
        $earliest = $INF;
        $latest = -$INF;
        foreach ($this->g[$i] as $j) {
            $a = $this->dfs($j);
            $earliest = min($earliest, $a);
            $latest = max($latest, $a);
        }
        $ownDuration = ($latest - $earliest) + $this->baseTime[$i];
        return $latest + $ownDuration;
    }
}
