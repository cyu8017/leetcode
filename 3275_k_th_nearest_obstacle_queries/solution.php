<?php
// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

class Solution {
    function resultsArray($queries, $k) {
        $pq = new SplPriorityQueue();
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $d = abs($queries[$i][0]) + abs($queries[$i][1]);
            $pq->insert($d, $d);
            if ($pq->count() > $k) $pq->extract();
            $ans[$i] = $pq->count() < $k ? -1 : $pq->top();
        }
        return $ans;
    }
}
