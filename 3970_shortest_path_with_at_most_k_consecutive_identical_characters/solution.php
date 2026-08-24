<?php
// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

class Solution {
    function shortestPath($n, $edges, $labels, $k) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) $graph[$edge[0]][] = [$edge[1], $edge[2]];
        $infinity = PHP_INT_MAX / 4;
        $distances = array_fill(0, $n, array_fill(0, $k + 1, $infinity));
        $distances[0][1] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0, 1], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $distance = $cur[0];
            $node = $cur[1];
            $run = $cur[2];
            if ($distance !== $distances[$node][$run]) continue;
            if ($node === $n - 1) return $distance;
            foreach ($graph[$node] as $e) {
                $to = $e[0];
                $weight = $e[1];
                $nextRun = 1;
                if ($labels[$node] === $labels[$to]) $nextRun = $run + 1;
                if ($nextRun > $k) continue;
                $nextDistance = $distance + $weight;
                if ($nextDistance < $distances[$to][$nextRun]) {
                    $distances[$to][$nextRun] = $nextDistance;
                    $pq->insert([$nextDistance, $to, $nextRun], -$nextDistance);
                }
            }
        }
        return -1;
    }
}
