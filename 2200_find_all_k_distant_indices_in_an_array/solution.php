<?php
// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution {
    function findKDistantIndices($nums, $key, $k) {
        $n = count($nums);
        $mark = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === $key) {
                $l = max(0, $i - $k);
                $r = min($n - 1, $i + $k);
                for ($j = $l; $j <= $r; $j++) $mark[$j] = true;
            }
        }
        $ans = [];
        for ($i = 0; $i < $n; $i++) if ($mark[$i]) $ans[] = $i;
        return $ans;
    }
}
