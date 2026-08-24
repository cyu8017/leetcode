<?php
// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/

class Solution {
    function changeDatatype($students) {
        $out = [];
        foreach ($students as $r) {
            if (is_array($r) && isset($r[3]) && !isset($r['grade'])) $out[] = [$r[0], $r[1], $r[2], (int)$r[3]];
            else {
                $row = $r;
                $row['grade'] = (int)$r['grade'];
                $out[] = $row;
            }
        }
        return $out;
    }
}
