<?php
// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution {
    function intersection($nums) {
        $freq = [];
        foreach ($nums as $arr) {
            $seen = [];
            foreach ($arr as $x) {
                if (!isset($seen[$x])) {
                    $seen[$x] = true;
                    $freq[$x] = ($freq[$x] ?? 0) + 1;
                }
            }
        }
        $ans = [];
        foreach ($freq as $k => $v) if ($v === count($nums)) $ans[] = $k;
        sort($ans);
        return $ans;
    }
}
