<?php
// LeetCode 3892 - Minimum Operations to Achieve at Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

class Solution {
    public $cost;
    public $INF;
    function line($left, $right, $choose) {
        if ($choose === 0) return 0;
        if ($left > $right || $choose > intdiv($right - $left + 2, 2)) return $this->INF;
        $prev2 = array_fill(0, $choose + 1, $this->INF);
        $prev1 = array_fill(0, $choose + 1, $this->INF);
        $prev2[0] = $prev1[0] = 0;
        for ($i = $left; $i <= $right; $i++) {
            $current = $prev1;
            for ($j = 1; $j <= $choose; $j++) {
                if ($prev2[$j - 1] !== $this->INF && $prev2[$j - 1] + $this->cost[$i] < $current[$j]) {
                    $current[$j] = $prev2[$j - 1] + $this->cost[$i];
                }
            }
            $prev2 = $prev1;
            $prev1 = $current;
        }
        return $prev1[$choose];
    }
    function minOperations($nums, $k) {
        $this->INF = PHP_INT_MAX / 4;
        $n = count($nums);
        if ($k === 0) return 0;
        if ($k > intdiv($n, 2)) return -1;
        $this->cost = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $left = $nums[($i + $n - 1) % $n];
            $right = $nums[($i + 1) % $n];
            $need = max($left, $right);
            if ($need >= $nums[$i]) $this->cost[$i] = $need - $nums[$i] + 1;
        }
        $answer = $this->line(1, $n - 1, $k);
        $withFirst = $this->line(2, $n - 2, $k - 1);
        if ($withFirst !== $this->INF) {
            $withFirst += $this->cost[0];
            $answer = min($answer, $withFirst);
        }
        if ($answer === $this->INF) return -1;
        return $answer;
    }
}
