<?php
// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

class Solution {
    function passwordStrength($password) {
        $st = [];
        $n = strlen($password);
        for ($i = 0; $i < $n; $i++) $st[$password[$i]] = true;
        $ans = 0;
        foreach ($st as $ch => $_) {
            if (ctype_lower($ch)) $ans += 1;
            else if (ctype_upper($ch)) $ans += 2;
            else if (ctype_digit($ch)) $ans += 3;
            else $ans += 5;
        }
        return $ans;
    }
}
