<?php
// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function rotatedDigits($n) {
        $count = 0;
        for ($num = 1; $num <= $n; $num++) {
            $s = (string)$num;
            $ok = true;
            $changed = false;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $ch = $s[$i];
                if ($ch === '3' || $ch === '4' || $ch === '7') { $ok = false; break; }
                if ($ch === '2' || $ch === '5' || $ch === '6' || $ch === '9') $changed = true;
            }
            if ($ok && $changed) $count++;
        }
        return $count;
    }
}
