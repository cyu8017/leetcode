<?php
// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/

class Solution {
    function renameColumns($students) {
        $out = [];
        foreach ($students as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['id']) && !isset($r['first'])) {
                $out[] = [
                    'student_id' => $r[0],
                    'first_name' => $r[1],
                    'last_name' => $r[2],
                    'age_in_years' => $r[3],
                ];
            } else {
                $out[] = [
                    'student_id' => $r['id'],
                    'first_name' => $r['first'],
                    'last_name' => $r['last'],
                    'age_in_years' => $r['age'],
                ];
            }
        }
        return $out;
    }
}
