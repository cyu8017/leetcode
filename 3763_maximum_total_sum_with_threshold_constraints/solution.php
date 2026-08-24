<?php
// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

class Solution {
    function maxSum($nums, $threshold) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($threshold) {
            return $threshold[$a] <=> $threshold[$b];
        });
        $tree = [];
        $push = function($x) use (&$tree) {
            $tree[] = $x;
            $i = count($tree) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($tree[$i] <= $tree[$p]) break;
                $tmp = $tree[$i]; $tree[$i] = $tree[$p]; $tree[$p] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$tree) {
            $top = $tree[0];
            $last = array_pop($tree);
            if (count($tree)) {
                $tree[0] = $last;
                $i = 0;
                while (true) {
                    $s = $i;
                    $l = $i * 2 + 1;
                    $r = $l + 1;
                    if ($l < count($tree) && $tree[$l] > $tree[$s]) $s = $l;
                    if ($r < count($tree) && $tree[$r] > $tree[$s]) $s = $r;
                    if ($s === $i) break;
                    $tmp = $tree[$i]; $tree[$i] = $tree[$s]; $tree[$s] = $tmp;
                    $i = $s;
                }
            }
            return $top;
        };
        $ans = 0;
        $i = 0;
        for ($step = 1; ; $step++) {
            while ($i < $n && $threshold[$idx[$i]] <= $step) {
                $push($nums[$idx[$i]]);
                $i++;
            }
            if (!count($tree)) break;
            $ans += $pop();
        }
        return $ans;
    }
}
