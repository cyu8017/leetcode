<?php
// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

class Solution {
    function getFinalState($nums, $k, $multiplier) {
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $pq->insert($i, [-$nums[$i], -$i]);
        }
        for ($t = 0; $t < $k; $t++) {
            $item = $pq->extract();
            $i = $item['data'];
            $v = $nums[$i] * $multiplier;
            $nums[$i] = $v;
            $pq->insert($i, [-$v, -$i]);
        }
        return $nums;
    }
}
