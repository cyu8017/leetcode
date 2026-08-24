<?php
// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

class Solution {
    function maximumProduct($nums, $k) {
        $MOD = 1000000007;
        $pq = new SplPriorityQueue();
        foreach ($nums as $x) $pq->insert($x, -$x);
        for ($i = 0; $i < $k; $i++) {
            $x = $pq->extract();
            $pq->insert($x + 1, -($x + 1));
        }
        $ans = 1;
        while (!$pq->isEmpty()) $ans = $ans * $pq->extract() % $MOD;
        return $ans;
    }
}
