<?php
// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution {
    function minDeletionSize($strs) {
        $ans = 0;
        $m = strlen($strs[0]);
        $n = count($strs);
        for ($c = 0; $c < $m; $c++) {
            for ($r = 0; $r + 1 < $n; $r++) {
                if ($strs[$r][$c] > $strs[$r + 1][$c]) { $ans++; break; }
            }
        }
        return $ans;
    }
}
