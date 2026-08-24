<?php
// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution {
    private function popcount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function canSortArray($nums) {
        $preMx = 0;
        $i = 0;
        $n = count($nums);
        while ($i < $n) {
            $cnt = $this->popcount($nums[$i]);
            $j = $i + 1;
            $mi = $nums[$i];
            $mx = $nums[$i];
            while ($j < $n && $this->popcount($nums[$j]) === $cnt) {
                $mi = min($mi, $nums[$j]);
                $mx = max($mx, $nums[$j]);
                $j++;
            }
            if ($preMx > $mi) return false;
            $preMx = $mx;
            $i = $j;
        }
        return true;
    }
}
