<?php
// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

class Solution {
    function createGrid($m, $n) {
        $g = [];
        for ($i = 0; $i < $m; $i++) {
            $row = array_fill(0, $n, '#');
            if ($i == 0) {
                for ($j = 0; $j < $n; $j++) $row[$j] = '.';
            }
            $row[$n - 1] = '.';
            $g[] = implode('', $row);
        }
        return $g;
    }
}
