<?php
// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

class Solution {
    function maxSubtreeInversionSum($edges, $nums, $k) {
        $n = count($nums);
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $graph[$edge[0]][] = $edge[1];
            $graph[$edge[1]][] = $edge[0];
        }
        $parent = array_fill(0, $n, -2);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($graph[$u] as $v) {
                if ($parent[$v] === -2) {
                    $parent[$v] = $u;
                    $order[] = $v;
                }
            }
        }
        $infinity = 1 << 60;
        $maximum = array_fill(0, $n, null);
        $minimum = array_fill(0, $n, null);
        for ($oi = $n - 1; $oi >= 0; $oi--) {
            $u = $order[$oi];
            $currentMax = array_fill(0, $k + 1, -$infinity);
            $currentMin = array_fill(0, $k + 1, $infinity);
            $currentMax[$k] = $currentMin[$k] = $nums[$u];
            foreach ($graph[$u] as $v) {
                if ($parent[$v] !== $u) continue;
                $nextMax = array_fill(0, $k + 1, -$infinity);
                $nextMin = array_fill(0, $k + 1, $infinity);
                for ($first = 0; $first <= $k; $first++) {
                    if ($currentMax[$first] === -$infinity) continue;
                    for ($childDistance = 0; $childDistance <= $k; $childDistance++) {
                        if ($maximum[$v][$childDistance] === -$infinity) continue;
                        $second = $childDistance + 1;
                        if ($second > $k) $second = $k;
                        if ($first < $k && $second < $k && $first + $second < $k) continue;
                        $distance = min($first, $second);
                        $maxValue = $currentMax[$first] + $maximum[$v][$childDistance];
                        $minValue = $currentMin[$first] + $minimum[$v][$childDistance];
                        $nextMax[$distance] = max($nextMax[$distance], $maxValue);
                        $nextMin[$distance] = min($nextMin[$distance], $minValue);
                    }
                }
                $currentMax = $nextMax;
                $currentMin = $nextMin;
            }
            if (-$currentMin[$k] > $currentMax[0]) $currentMax[0] = -$currentMin[$k];
            if (-$currentMax[$k] < $currentMin[0]) $currentMin[0] = -$currentMax[$k];
            $maximum[$u] = $currentMax;
            $minimum[$u] = $currentMin;
        }
        $answer = -(1 << 60);
        foreach ($maximum[0] as $value) $answer = max($answer, $value);
        return $answer;
    }
}
