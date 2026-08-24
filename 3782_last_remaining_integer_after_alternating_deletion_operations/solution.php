<?php
// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

class Solution {
    function lastRemaining($n) {
        $first = 1;
        $step = 2;
        $left = true;
        while ($n > 1) {
            if (!$left && $n % 2 === 0) $first += $step;
            $n = intdiv($n + 1, 2);
            $step *= 2;
            $left = !$left;
        }
        return $first;
    }
}
