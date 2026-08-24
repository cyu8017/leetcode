<?php
// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

class Solution {
    function modifySalaryColumn($employees) {
        $out = [];
        foreach ($employees as $r) {
            if (is_array($r) && isset($r[1]) && !isset($r['salary'])) $out[] = [$r[0], $r[1] * 2];
            else {
                $row = $r;
                $row['salary'] = $r['salary'] * 2;
                $out[] = $row;
            }
        }
        return $out;
    }
}
