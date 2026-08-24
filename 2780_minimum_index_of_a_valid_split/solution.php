<?php
// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution {
    function minimumIndex($nums) {
        $freq = [];
        $dom = 0;
        $best = 0;
        foreach ($nums as $v) {
            $c = ($freq[$v] ?? 0) + 1;
            $freq[$v] = $c;
            if ($c > $best) { $best = $c; $dom = $v; }
        }
        $left = 0;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] === $dom) $left++;
            $right = $best - $left;
            if ($left * 2 > $i + 1 && $right * 2 > $n - $i - 1) return $i;
        }
        return -1;
    }
}
