<?php
// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

class Solution {
    function numUniqueEmails($emails) {
        $set = [];
        foreach ($emails as $email) {
            [$local, $domain] = explode("@", $email, 2);
            $cleaned = "";
            $len = strlen($local);
            for ($i = 0; $i < $len; $i++) {
                if ($local[$i] === "+") break;
                if ($local[$i] !== ".") $cleaned .= $local[$i];
            }
            $set[$cleaned . "@" . $domain] = true;
        }
        return count($set);
    }
}
