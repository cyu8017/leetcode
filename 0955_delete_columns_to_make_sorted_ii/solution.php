<?php
// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution {
    function minDeletionSize($strs) {
        $n = count($strs);
        $m = strlen($strs[0]);
        $deleted = 0;
        $sortedPair = array_fill(0, $n - 1, false);
        for ($c = 0; $c < $m; $c++) {
            $bad = false;
            for ($r = 0; $r + 1 < $n; $r++) {
                if (!$sortedPair[$r] && $strs[$r][$c] > $strs[$r + 1][$c]) { $bad = true; break; }
            }
            if ($bad) { $deleted++; continue; }
            for ($r = 0; $r + 1 < $n; $r++) {
                if ($strs[$r][$c] < $strs[$r + 1][$c]) $sortedPair[$r] = true;
            }
        }
        return $deleted;
    }
}
