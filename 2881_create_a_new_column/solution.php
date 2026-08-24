<?php
// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

class Solution {
    function createBonusColumn($employees) {
        $out = [];
        foreach ($employees as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['name']) && !isset($r['salary'])) {
                $out[] = ['name' => $r[0], 'salary' => $r[1], 'bonus' => $r[1] * 2];
            } else {
                $row = $r;
                $row['bonus'] = $r['salary'] * 2;
                $out[] = $row;
            }
        }
        return $out;
    }
}
