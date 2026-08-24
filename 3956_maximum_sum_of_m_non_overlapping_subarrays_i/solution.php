<?php
// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

class Solution {
    function maxSum($nums, $m, $l, $r) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $dp = array_fill(0, $n + 1, 0);
        $bestSelected = -(1 << 62);
        for ($count = 1; $count <= $m; $count++) {
            $next = $dp;
            $deque = [];
            for ($end = 1; $end <= $n; $end++) {
                $addIndex = $end - $l;
                if ($addIndex >= 0) {
                    $value = $dp[$addIndex] - $prefix[$addIndex];
                    while (count($deque) > 0) {
                        $last = $deque[count($deque) - 1];
                        if ($dp[$last] - $prefix[$last] > $value) break;
                        array_pop($deque);
                    }
                    $deque[] = $addIndex;
                }
                $minIndex = $end - $r;
                while (count($deque) > 0 && $deque[0] < $minIndex) array_shift($deque);
                if (count($deque) > 0) {
                    $candidate = $prefix[$end] + $dp[$deque[0]] - $prefix[$deque[0]];
                    if ($candidate > $next[$end]) $next[$end] = $candidate;
                    if ($candidate > $bestSelected) $bestSelected = $candidate;
                }
                if ($next[$end - 1] > $next[$end]) $next[$end] = $next[$end - 1];
            }
            $dp = $next;
        }
        return $bestSelected;
    }
}
