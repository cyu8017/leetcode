<?php
// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

class Solution {
    function dropMissingData($students) {
        $out = [];
        foreach ($students as $r) {
            $name = (is_array($r) && isset($r[1]) && !isset($r['name'])) ? $r[1] : ($r['name'] ?? null);
            if ($name !== null && $name !== '') $out[] = $r;
        }
        return $out;
    }
}
