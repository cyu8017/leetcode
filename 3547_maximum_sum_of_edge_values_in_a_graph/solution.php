<?php
// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

class Solution {
    private function calc($left, $right, $isCycle) {
        $w0 = $right;
        $w1 = $right;
        $score = 0;
        for ($value = $right - 1; $value >= $left; $value--) {
            $score += $w0 * $value;
            $w0 = $w1;
            $w1 = $value;
        }
        if ($isCycle) $score += $w0 * $w1;
        return $score;
    }

    private function getComp($start, $graph, &$seen) {
        $comp = [$start];
        $seen[$start] = true;
        for ($i = 0; $i < count($comp); $i++) {
            foreach ($graph[$comp[$i]] as $v) {
                if (!$seen[$v]) { $seen[$v] = true; $comp[] = $v; }
            }
        }
        return $comp;
    }

    function maxScore($n, $edges) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = $e[1];
            $graph[$e[1]][] = $e[0];
        }
        $seen = array_fill(0, $n, false);
        $cycleSizes = [];
        $pathSizes = [];
        for ($i = 0; $i < $n; $i++) {
            if ($seen[$i]) continue;
            $comp = $this->getComp($i, $graph, $seen);
            $allDeg2 = true;
            foreach ($comp as $u) if (count($graph[$u]) !== 2) { $allDeg2 = false; break; }
            if ($allDeg2) $cycleSizes[] = count($comp);
            else if (count($comp) > 1) $pathSizes[] = count($comp);
        }
        $ans = 0;
        $curN = $n;
        foreach ($cycleSizes as $cs) {
            $ans += $this->calc($curN - $cs + 1, $curN, true);
            $curN -= $cs;
        }
        rsort($pathSizes);
        foreach ($pathSizes as $ps) {
            $ans += $this->calc($curN - $ps + 1, $curN, false);
            $curN -= $ps;
        }
        return $ans;
    }
}
