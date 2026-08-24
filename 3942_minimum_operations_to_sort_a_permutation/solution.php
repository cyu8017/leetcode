<?php
// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

class Solution {
    function minOperations($nums) {
        $n = count($nums);
        $zero = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] == 0) {
                $zero = $i;
                break;
            }
        }
        $ans = 2147483647;
        if ($this->check($nums, $zero, 1)) {
            $ans = min($ans, $zero);
            $ans = min($ans, $n - $zero + 2);
        }
        if ($this->check($nums, $zero, -1)) {
            $ans = min($ans, $zero + 2);
            $ans = min($ans, $n - $zero);
        }
        return $ans == 2147483647 ? -1 : $ans;
    }

    private function check($nums, $zero, $step) {
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $prev = (($zero + ($i - 1) * $step) % $n + $n) % $n;
            $curr = (($zero + $i * $step) % $n + $n) % $n;
            if ($nums[$prev] > $nums[$curr]) return false;
        }
        return true;
    }
}
