<?php
// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

class Solution {
    private function gaps($fences, $bound) {
        $list = array_merge([1], $fences, [$bound]);
        sort($list);
        $g = [];
        $n = count($list);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $g[$list[$j] - $list[$i]] = true;
            }
        }
        return $g;
    }

    function maximizeSquareArea($m, $n, $hFences, $vFences) {
        $mod = 1000000007;
        $hg = $this->gaps($hFences, $m);
        $vg = $this->gaps($vFences, $n);
        $best = -1;
        foreach ($hg as $g => $_) {
            if (isset($vg[$g]) && $g > $best) $best = $g;
        }
        if ($best < 0) return -1;
        return (int)(($best * $best) % $mod);
    }
}
