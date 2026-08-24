<?php
// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution {
    function minDeletionSize($strs) {
        $m = strlen($strs[0]);
        $dp = array_fill(0, $m, 1);
        for ($j = 0; $j < $m; $j++) {
            for ($i = 0; $i < $j; $i++) {
                $ok = true;
                foreach ($strs as $row) {
                    if ($row[$i] > $row[$j]) { $ok = false; break; }
                }
                if ($ok) $dp[$j] = max($dp[$j], $dp[$i] + 1);
            }
        }
        return $m - max($dp);
    }
}
