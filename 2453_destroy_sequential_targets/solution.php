<?php
// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

class Solution {
    function destroyTargets($nums, $space) {
        $cnt = [];
        foreach ($nums as $x) {
            $m = $x % $space;
            if (!isset($cnt[$m])) $cnt[$m] = 0;
            $cnt[$m]++;
        }
        $bestCnt = 0;
        foreach ($cnt as $c) if ($c > $bestCnt) $bestCnt = $c;
        $ans = 1000000000;
        foreach ($cnt as $key => $value) {
            if ($value === $bestCnt) {
                foreach ($nums as $x) {
                    if ($x % $space == $key && $x < $ans) $ans = $x;
                }
            }
        }
        return $ans;
    }
}
