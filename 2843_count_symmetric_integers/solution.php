<?php
// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

class Solution {
    function countSymmetricIntegers($low, $high) {
        $ans = 0;
        for ($x = $low; $x <= $high; $x++) {
            $s = (string)$x;
            $len = strlen($s);
            if ($len % 2 !== 0) continue;
            $mid = intdiv($len, 2);
            $a = 0;
            $b = 0;
            for ($i = 0; $i < $mid; $i++) {
                $a += ord($s[$i]) - 48;
                $b += ord($s[$mid + $i]) - 48;
            }
            if ($a === $b) $ans++;
        }
        return $ans;
    }
}
