<?php
// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/

class Solution {
    function fillMissingValues($products) {
        $out = [];
        foreach ($products as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['quantity'])) {
                $q = $r[1] ?? 0;
                if ($q === null) $q = 0;
                $out[] = [$r[0], $q, $r[2] ?? null];
            } else {
                $row = $r;
                $row['quantity'] = ($r['quantity'] ?? null) === null ? 0 : $r['quantity'];
                $out[] = $row;
            }
        }
        return $out;
    }
}
