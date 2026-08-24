<?php
// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

class Solution {
    function zigzagTraversal($grid) {
        $ans = [];
        $skip = false;
        $m = count($grid);
        for ($i = 0; $i < $m; $i++) {
            $row = $grid[$i];
            if ($i % 2 === 0) {
                foreach ($row as $v) {
                    if (!$skip) $ans[] = $v;
                    $skip = !$skip;
                }
            } else {
                for ($j = count($row) - 1; $j >= 0; $j--) {
                    if (!$skip) $ans[] = $row[$j];
                    $skip = !$skip;
                }
            }
        }
        return $ans;
    }
}
