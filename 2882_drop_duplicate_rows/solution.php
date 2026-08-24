<?php
// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/

class Solution {
    function dropDuplicateEmails($customers) {
        $seen = [];
        $out = [];
        foreach ($customers as $r) {
            $email = (is_array($r) && isset($r[2]) && !isset($r['email'])) ? $r[2] : $r['email'];
            if (isset($seen[$email])) continue;
            $seen[$email] = true;
            $out[] = $r;
        }
        return $out;
    }
}
