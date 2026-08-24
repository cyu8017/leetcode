<?php
// LeetCode 0420 - Strong Password Checker
// https://leetcode.com/problems/strong-password-checker/

class Solution {
    /**
     * @param String $password
     * @return Integer
     */
    function strongPasswordChecker($password) {
        return $this->strong_password_checker($password);
    }

    /**
     * @param String $password
     * @return Integer
     */
    function strong_password_checker($password) {
        $length = strlen($password);
        $missing = 3;
        if (preg_match('/[a-z]/', $password)) {
            $missing--;
        }
        if (preg_match('/[A-Z]/', $password)) {
            $missing--;
        }
        if (preg_match('/\d/', $password)) {
            $missing--;
        }

        $replace = 0;
        $oneRepeat = 0;
        $twoRepeat = 0;
        $index = 0;
        while ($index < $length) {
            $run = 1;
            while ($index + $run < $length && $password[$index + $run] === $password[$index]) {
                $run++;
            }
            if ($run >= 3) {
                $replace += intdiv($run, 3);
                if ($run % 3 === 0) {
                    $oneRepeat++;
                } elseif ($run % 3 === 1) {
                    $twoRepeat++;
                }
            }
            $index += $run;
        }

        if ($length < 6) {
            return max(6 - $length, $missing);
        }
        if ($length <= 20) {
            return max($missing, $replace);
        }

        $delete = $length - 20;
        $replace -= min($delete, $oneRepeat);
        $delete -= min($delete, $oneRepeat);
        $replace -= min(intdiv($delete, 2), $twoRepeat);
        $delete -= min(intdiv($delete, 2), $twoRepeat) * 2;
        $replace -= intdiv($delete, 3);
        return $length - 20 + max($missing, $replace);
    }
}
