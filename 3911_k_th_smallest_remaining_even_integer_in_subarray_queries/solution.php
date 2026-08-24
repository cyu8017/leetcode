<?php
// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

class Solution {
    function UpperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
    function kthSmallestEven($nums, $queries) {
        $n = count($nums);
        $evenPrefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $evenPrefix[$i + 1] = $evenPrefix[$i] + ($nums[$i] % 2 === 0 ? 1 : 0);
        }
        $ans = [];
        $qn = count($queries);
        for ($qi = 0; $qi < $qn; $qi++) {
            $l = $queries[$qi][0];
            $r = $queries[$qi][1];
            $k = $queries[$qi][2];
            $lo = 1;
            $hi = $k + ($r - $l + 1);
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                $pos = $this->UpperBound($nums, 2 * $mid);
                if ($pos > $r + 1) $pos = $r + 1;
                $removed = 0;
                if ($pos > $l) $removed = $evenPrefix[$pos] - $evenPrefix[$l];
                if ($mid - $removed >= $k) $hi = $mid;
                else $lo = $mid + 1;
            }
            $ans[$qi] = 2 * $lo;
        }
        return $ans;
    }
}
