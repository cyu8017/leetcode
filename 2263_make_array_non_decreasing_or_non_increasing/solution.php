<?php
// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

class Solution {
    function solve($nums) {
        $cost = function($arr) {
            $pq = new SplPriorityQueue();
            $ans = 0;
            foreach ($arr as $x) {
                if (!$pq->isEmpty() && $pq->top() > $x) {
                    $t = $pq->extract();
                    $ans += $t - $x;
                    $pq->insert($x, $x);
                }
                $pq->insert($x, $x);
            }
            return $ans;
        };
        $rev = array_reverse($nums);
        return min($cost($nums), $cost($rev));
    }
}
