<?php
// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

class Solution {
    function smallestProperDivisor($x) {
        for ($d = 2; $d * $d <= $x; $d++) if ($x % $d === 0) return $d;
        return $x;
    }

    function minOperations($nums) {
        $ops = 0;
        for ($i = count($nums) - 2; $i >= 0; $i--) {
            if ($nums[$i] <= $nums[$i + 1]) continue;
            while ($nums[$i] > $nums[$i + 1]) {
                $d = $this->smallestProperDivisor($nums[$i]);
                if ($d === $nums[$i]) return -1;
                $nums[$i] = intdiv($nums[$i], $d);
                $ops++;
                if ($nums[$i] > $nums[$i + 1] && $this->smallestProperDivisor($nums[$i]) === $nums[$i]) return -1;
            }
        }
        return $ops;
    }
}
