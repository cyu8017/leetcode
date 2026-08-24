<?php
// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

class Solution {
    private function opsToZero($x) {
        $ops = 0;
        while ($x > 0) { $x = intdiv($x, 4); $ops++; }
        return $ops;
    }

    function minOperations($queries) {
        $ans = 0;
        foreach ($queries as $q) {
            $l = $q[0];
            $r = $q[1];
            $sum = 0;
            for ($x = $l; $x <= $r; $x++) $sum += $this->opsToZero($x);
            $ans += intdiv($sum + 1, 2);
        }
        return $ans;
    }
}
