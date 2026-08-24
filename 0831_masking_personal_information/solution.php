<?php
// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function maskPII($s) {
        $at = strpos($s, '@');
        if ($at !== false) {
            $s = strtolower($s);
            $at = strpos($s, '@');
            $name = substr($s, 0, $at);
            $domain = substr($s, $at + 1);
            return $name[0] . "*****" . $name[strlen($name) - 1] . "@" . $domain;
        }
        $digits = "";
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if (ctype_digit($s[$i])) $digits .= $s[$i];
        }
        $local = substr($digits, -4);
        $country = strlen($digits) - 10;
        if ($country === 0) return "***-***-" . $local;
        return "+" . str_repeat("*", $country) . "-***-***-" . $local;
    }
}
