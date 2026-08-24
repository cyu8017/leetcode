<?php
// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

class Solution {
    function strongPasswordCheckerII($password) {
        if (strlen($password) < 8) return false;
        $special = '!@#$%^&*()-+';
        $hasLower = false;
        $hasUpper = false;
        $hasDigit = false;
        $hasSpecial = false;
        $n = strlen($password);
        for ($i = 0; $i < $n; $i++) {
            $c = $password[$i];
            if ($i > 0 && $c === $password[$i - 1]) return false;
            if ($c >= 'a' && $c <= 'z') $hasLower = true;
            else if ($c >= 'A' && $c <= 'Z') $hasUpper = true;
            else if ($c >= '0' && $c <= '9') $hasDigit = true;
            else if (strpos($special, $c) !== false) $hasSpecial = true;
        }
        return $hasLower && $hasUpper && $hasDigit && $hasSpecial;
    }
}
