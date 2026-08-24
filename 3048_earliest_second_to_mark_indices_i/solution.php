<?php
// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

class Solution {
    function earliestSecondToMarkIndices($nums, $changeIndices) {
        $n = count($nums);
        $m = count($changeIndices);
        $ok = function($t) use ($nums, $changeIndices, $n) {
            $last = array_fill(0, $n + 1, 0);
            for ($s = 0; $s < $t; $s++) $last[$changeIndices[$s]] = $s;
            $decrement = 0;
            $marked = 0;
            for ($s = 0; $s < $t; $s++) {
                $i = $changeIndices[$s];
                if ($last[$i] === $s) {
                    if ($decrement < $nums[$i - 1]) return false;
                    $decrement -= $nums[$i - 1];
                    $marked++;
                } else {
                    $decrement++;
                }
            }
            return $marked === $n;
        };
        $l = 0;
        $r = $m + 1;
        while ($l < $r) {
            $mid = ($l + $r) >> 1;
            if ($ok($mid)) $r = $mid;
            else $l = $mid + 1;
        }
        return $l > $m ? -1 : $l;
    }
}
