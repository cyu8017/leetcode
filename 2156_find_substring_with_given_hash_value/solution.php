<?php
// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

class Solution {
    /**
     * @param String $s
     * @param Integer $power
     * @param Integer $modulo
     * @param Integer $k
     * @param Integer $hashValue
     * @return String
     */
    function subStrHash($s, $power, $modulo, $k, $hashValue) {
        $n = strlen($s);
        $pk = 1;
        for ($i = 0; $i < $k - 1; $i++) $pk = ($pk * $power) % $modulo;
        $h = 0;
        $ans = 0;
        for ($i = $n - 1; $i >= $n - $k; $i--)
            $h = ($h * $power + (ord($s[$i]) - 96)) % $modulo;
        if ($h === $hashValue) $ans = $n - $k;
        for ($i = $n - $k - 1; $i >= 0; $i--) {
            $h = ($h - ((ord($s[$i + $k]) - 96) * $pk % $modulo) + $modulo) % $modulo;
            $h = ($h * $power + (ord($s[$i]) - 96)) % $modulo;
            if ($h === $hashValue) $ans = $i;
        }
        return substr($s, $ans, $k);
    }
}
