<?php
// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

class Solution {
    function maxAlternatingSum($nums, $swaps) {
        $n = count($nums);
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($swaps as $s) {
            $a = $find($s[0]);
            $b = $find($s[1]);
            if ($a !== $b) $parent[$a] = $b;
        }
        $compVals = [];
        $compIdx = [];
        for ($i = 0; $i < $n; $i++) {
            $r = $find($i);
            if (!isset($compVals[$r])) { $compVals[$r] = []; $compIdx[$r] = []; }
            $compVals[$r][] = $nums[$i];
            $compIdx[$r][] = $i;
        }
        $arr = array_fill(0, $n, 0);
        foreach ($compVals as $r => $vals) {
            $idxs = $compIdx[$r];
            rsort($vals);
            $even = [];
            $odd = [];
            foreach ($idxs as $i) {
                if ($i % 2 === 0) $even[] = $i;
                else $odd[] = $i;
            }
            sort($even);
            sort($odd);
            $ei = 0;
            $en = count($even);
            foreach ($vals as $v) {
                if ($ei < $en) {
                    $arr[$even[$ei]] = $v;
                    $ei++;
                } else {
                    $arr[$odd[$ei - $en]] = $v;
                    $ei++;
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $ans += $arr[$i];
            else $ans -= $arr[$i];
        }
        return $ans;
    }
}
