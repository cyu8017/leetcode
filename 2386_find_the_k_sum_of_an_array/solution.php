<?php
// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

class Solution {
    function kSum($nums, $k) {
        $total = 0;
        $n = count($nums);
        $absNums = [];
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] >= 0) {
                $total += $nums[$i];
                $absNums[] = $nums[$i];
            } else {
                $absNums[] = -$nums[$i];
            }
        }
        sort($absNums);
        $h = new SplPriorityQueue();
        $h->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $h->insert([$total, 0], $total);
        for ($t = 0; $t < $k - 1; $t++) {
            $cur = $h->extract();
            $sum = $cur[0];
            $i = $cur[1];
            if ($i >= count($absNums)) continue;
            $h->insert([$sum - $absNums[$i], $i + 1], $sum - $absNums[$i]);
            if ($i > 0) {
                $h->insert([$sum - $absNums[$i] + $absNums[$i - 1], $i + 1], $sum - $absNums[$i] + $absNums[$i - 1]);
            }
        }
        $top = $h->top();
        return $top[0];
    }
}
