<?php
// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

class Solution {
    function maxRemoval($nums, $queries) {
        usort($queries, function($a, $b) { return $a[0] <=> $b[0]; });
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        $j = 0;
        $used = 0;
        $cur = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            while ($j < count($queries) && $queries[$j][0] === $i) {
                $pq->insert($queries[$j][1], $queries[$j][1]);
                $j++;
            }
            while ($cur < $nums[$i]) {
                if ($pq->isEmpty()) return -1;
                $r = $pq->extract();
                if ($r < $i) return -1;
                $cur++;
                $diff[$r + 1]--;
                $used++;
            }
        }
        return count($queries) - $used;
    }
}
