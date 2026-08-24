<?php
// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        $n = count($nums);
        if ($n === 1) return 0;
        $top2 = function($idxs) use ($nums) {
            $freq = [];
            foreach ($idxs as $i) $freq[$nums[$i]] = ($freq[$nums[$i]] ?? 0) + 1;
            $a = 0; $ac = 0; $b = 0; $bc = 0;
            foreach ($freq as $v => $c) {
                if ($c > $ac) { $b = $a; $bc = $ac; $a = $v; $ac = $c; }
                else if ($c > $bc) { $b = $v; $bc = $c; }
            }
            return [$a, $ac, $b, $bc];
        };
        $even = [];
        $odd = [];
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) $even[] = $i;
            else $odd[] = $i;
        }
        $e = $top2($even);
        $o = $top2($odd);
        if ($e[0] !== $o[0]) return $n - $e[1] - $o[1];
        return min($n - $e[1] - $o[3], $n - $e[3] - $o[1]);
    }
}
