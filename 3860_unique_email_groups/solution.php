<?php
// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

class Solution {
    function uniqueEmailGroups($emails) {
        $st = [];
        foreach ($emails as $email) {
            $at = strpos($email, '@');
            $local = substr($email, 0, $at);
            $domain = strtolower(substr($email, $at + 1));
            $plus = strpos($local, '+');
            if ($plus !== false) $local = substr($local, 0, $plus);
            $cleaned = '';
            $len = strlen($local);
            for ($i = 0; $i < $len; $i++) {
                $c = $local[$i];
                if ($c !== '.') $cleaned .= strtolower($c);
            }
            $st[$cleaned . $domain] = true;
        }
        return count($st);
    }
}
