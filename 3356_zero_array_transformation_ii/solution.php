<?php
// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

class Solution {
    function ok($k, $nums, $queries, $n) {
        $diff = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $k; $i++) {
            $q = $queries[$i];
            $diff[$q[0]] += $q[2];
            $diff[$q[1] + 1] -= $q[2];
        }
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            if ($cur < $nums[$i]) return false;
        }
        return true;
    }

    function minZeroArray($nums, $queries) {
        $n = count($nums);
        if ($this->ok(0, $nums, $queries, $n)) return 0;
        $lo = 1;
        $hi = count($queries) + 1;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($mid <= count($queries) && $this->ok($mid, $nums, $queries, $n)) $hi = $mid;
            else $lo = $mid + 1;
        }
        if ($lo > count($queries)) return -1;
        return $lo;
    }
}
