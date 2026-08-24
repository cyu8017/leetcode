<?php
// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution {
    function maxKelements($nums, $k) {
        $pq = new SplPriorityQueue();
        foreach ($nums as $x) $pq->insert($x, $x);
        $ans = 0;
        for ($i = 0; $i < $k; $i++) {
            $x = $pq->extract();
            $ans += $x;
            $nxt = intdiv($x + 2, 3);
            $pq->insert($nxt, $nxt);
        }
        return $ans;
    }
}
