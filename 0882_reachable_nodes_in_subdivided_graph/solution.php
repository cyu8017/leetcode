<?php
// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

class Solution {
    function reachableNodes($edges, $maxMoves, $n) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][$e[1]] = $e[2];
            $graph[$e[1]][$e[0]] = $e[2];
        }
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert(0, $maxMoves);
        $seen = [];
        while (!$pq->isEmpty()) {
            $item = $pq->extract();
            $node = $item['data'];
            $moves = $item['priority'];
            if (array_key_exists($node, $seen)) continue;
            $seen[$node] = $moves;
            foreach ($graph[$node] as $nei => $dist) {
                $remain = $moves - $dist - 1;
                if (!array_key_exists($nei, $seen) && $remain >= 0) {
                    $pq->insert($nei, $remain);
                }
            }
        }
        $ans = count($seen);
        foreach ($edges as $e) {
            $left = $seen[$e[0]] ?? 0;
            $right = $seen[$e[1]] ?? 0;
            $ans += min($e[2], $left + $right);
        }
        return $ans;
    }
}
