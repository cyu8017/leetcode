<?php
// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution {
    function countBadPairs($nums) {
        $n = count($nums);
        $total = intdiv($n * ($n - 1), 2);
        $freq = [];
        $good = 0;
        for ($i = 0; $i < $n; $i++) {
            $key = $nums[$i] - $i;
            $good += $freq[$key] ?? 0;
            $freq[$key] = ($freq[$key] ?? 0) + 1;
        }
        return $total - $good;
    }
}
