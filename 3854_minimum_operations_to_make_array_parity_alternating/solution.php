<?php
// LeetCode 3854 - Minimum Operations to Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

class Solution {
    function f($nums, $k, $mn, $mx) {
        $cnt = 0;
        $a = PHP_INT_MAX;
        $b = PHP_INT_MIN;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ((($x - $i) & 1) !== $k) {
                $cnt++;
                if ($x === $mn) $x++;
                else if ($x === $mx) $x--;
            }
            $a = min($a, $x);
            $b = max($b, $x);
        }
        return [$cnt, max(1, $b - $a)];
    }
    function makeParityAlternating($nums) {
        if (count($nums) === 1) return [0, 0];
        $mn = $nums[0];
        $mx = $nums[0];
        foreach ($nums as $x) { $mn = min($mn, $x); $mx = max($mx, $x); }
        $r0 = $this->f($nums, 0, $mn, $mx);
        $r1 = $this->f($nums, 1, $mn, $mx);
        if ($r0[0] !== $r1[0]) return $r0[0] < $r1[0] ? $r0 : $r1;
        return $r0[1] <= $r1[1] ? $r0 : $r1;
    }
}
