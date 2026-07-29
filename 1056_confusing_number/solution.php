<?php
// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function confusingNumber($n) {
        $rotate = ["0" => "0", "1" => "1", "6" => "9", "8" => "8", "9" => "6"];
        $s = (string)$n;
        $rotated = "";
        for ($i = strlen($s) - 1; $i >= 0; $i--) {
            $ch = $s[$i];
            if (!isset($rotate[$ch])) {
                return false;
            }
            $rotated .= $rotate[$ch];
        }
        return $rotated !== $s;
    }
}
