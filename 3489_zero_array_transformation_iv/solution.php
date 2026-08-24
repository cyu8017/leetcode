<?php
// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

class Solution {
    private function canSubsetSum($vals, $target) {
        if ($target === 0) return true;
        $dp = array_fill(0, $target + 1, false);
        $dp[0] = true;
        foreach ($vals as $v) {
            for ($s = $target; $s >= $v; $s--) if ($dp[$s - $v]) $dp[$s] = true;
        }
        return $dp[$target];
    }

    function minZeroArray($nums, $queries) {
        $ok = function($k) use ($nums, $queries) {
            for ($i = 0; $i < count($nums); $i++) {
                if ($nums[$i] === 0) continue;
                $vals = [];
                for ($q = 0; $q < $k; $q++) {
                    $l = $queries[$q][0];
                    $r = $queries[$q][1];
                    $v = $queries[$q][2];
                    if ($l <= $i && $i <= $r) $vals[] = $v;
                }
                if (!$this->canSubsetSum($vals, $nums[$i])) return false;
            }
            return true;
        };
        if ($ok(0)) return 0;
        $lo = 1;
        $hi = count($queries) + 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($mid <= count($queries) && $ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo > count($queries) ? -1 : $lo;
    }
}
