<?php
// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

class Solution {
    function minFinishTime($n, $edges, $baseTime) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $iu = count($graph[$u]);
            $iv = count($graph[$v]);
            $graph[$u][] = [$v, $iv];
            $graph[$v][] = [$u, $iu];
        }
        $parent = array_fill(0, $n, -2);
        $parentEdge = array_fill(0, $n, 0);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($graph[$u] as $edge) {
                if ($parent[$edge[0]] === -2) {
                    $parent[$edge[0]] = $u;
                    $parentEdge[$edge[0]] = $edge[1];
                    $order[] = $edge[0];
                }
            }
        }
        $incoming = [];
        for ($i = 0; $i < $n; $i++) $incoming[$i] = array_fill(0, count($graph[$i]), 0);
        for ($oi = $n - 1; $oi > 0; $oi--) {
            $u = $order[$oi];
            $minimum = 1 << 62;
            $maximum = -1;
            $count = 0;
            for ($edgeIndex = 0; $edgeIndex < count($incoming[$u]); $edgeIndex++) {
                if ($edgeIndex === $parentEdge[$u]) continue;
                $value = $incoming[$u][$edgeIndex];
                $minimum = min($minimum, $value);
                $maximum = max($maximum, $value);
                $count++;
            }
            $value = $this->combine($minimum, $maximum, $count, $baseTime[$u]);
            $parentNode = $parent[$u];
            $reverseIndex = $graph[$u][$parentEdge[$u]][1];
            $incoming[$parentNode][$reverseIndex] = $value;
        }
        $answer = 1 << 62;
        foreach ($order as $u) {
            $min1 = 1 << 62;
            $min2 = 1 << 62;
            $minIndex = -1;
            $max1 = -1;
            $max2 = -1;
            $maxIndex = -1;
            for ($i = 0; $i < count($incoming[$u]); $i++) {
                $value = $incoming[$u][$i];
                if ($value < $min1) {
                    $min2 = $min1;
                    $min1 = $value;
                    $minIndex = $i;
                } else if ($value < $min2) $min2 = $value;
                if ($value > $max1) {
                    $max2 = $max1;
                    $max1 = $value;
                    $maxIndex = $i;
                } else if ($value > $max2) $max2 = $value;
            }
            $rootValue = $this->combine($min1, $max1, count($graph[$u]), $baseTime[$u]);
            $answer = min($answer, $rootValue);
            for ($i = 0; $i < count($graph[$u]); $i++) {
                $edge = $graph[$u][$i];
                if ($edge[0] === $parent[$u]) continue;
                if (count($graph[$u]) === 1) {
                    $incoming[$edge[0]][$edge[1]] = $baseTime[$u];
                    continue;
                }
                $minimum = $min1;
                $maximum = $max1;
                if ($i === $minIndex) $minimum = $min2;
                if ($i === $maxIndex) $maximum = $max2;
                $incoming[$edge[0]][$edge[1]] = $this->combine($minimum, $maximum, count($graph[$u]) - 1, $baseTime[$u]);
            }
        }
        return $answer;
    }

    private function combine($minimum, $maximum, $count, $base) {
        if ($count === 0) return $base;
        return 2 * $maximum - $minimum + $base;
    }
}
