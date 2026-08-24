<?php
// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

class Solution {
    function maximumScore($nums, $s) {
        $ans = 0;
        $pq = new SplPriorityQueue();
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $pq->insert($nums[$i], $nums[$i]);
            if ($s[$i] === '1') $ans += $pq->extract();
        }
        return $ans;
    }
}
