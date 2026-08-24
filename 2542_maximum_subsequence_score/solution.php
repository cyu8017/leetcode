<?php
// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

class Solution {
    function maxScore($nums1, $nums2, $k) {
        $n = count($nums1);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($nums2) { return $nums2[$b] <=> $nums2[$a]; });
        $pq = new SplPriorityQueue();
        $sum = 0;
        $ans = 0;
        foreach ($idx as $i) {
            $pq->insert($nums1[$i], -$nums1[$i]);
            $sum += $nums1[$i];
            if ($pq->count() > $k) $sum -= $pq->extract();
            if ($pq->count() === $k) {
                $cand = $sum * $nums2[$i];
                if ($cand > $ans) $ans = $cand;
            }
        }
        return $ans;
    }
}
