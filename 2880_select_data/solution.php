<?php
// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/

class Solution {
    function selectData($students) {
        $out = [];
        foreach ($students as $r) {
            $id = is_array($r) && isset($r[0]) && !isset($r['student_id']) ? $r[0] : ($r['student_id'] ?? null);
            if ($id !== 101) continue;
            if (is_array($r) && isset($r[1]) && !isset($r['name'])) $out[] = ['name' => $r[1], 'age' => $r[2]];
            else $out[] = ['name' => $r['name'], 'age' => $r['age']];
        }
        return $out;
    }
}
