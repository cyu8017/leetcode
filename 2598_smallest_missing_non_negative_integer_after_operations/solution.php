<?php
// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

class Solution {
    function findSmallestInteger($nums, $value) {
        $cnt = array_fill(0, $value, 0);
        foreach ($nums as $x) {
            $r = $x % $value;
            if ($r < 0) $r += $value;
            $cnt[$r]++;
        }
        $mex = 0;
        while ($cnt[$mex % $value] > 0) {
            $cnt[$mex % $value]--;
            $mex++;
        }
        return $mex;
    }
}
