<?php
// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

class Solution {
    function decodeAtIndex($s, $k) {
        $size = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch >= '0' && $ch <= '9') $size *= ord($ch) - 48;
            else $size++;
        }
        $kk = $k;
        for ($i = $n - 1; $i >= 0; $i--) {
            $ch = $s[$i];
            $kk %= $size;
            if ($kk === 0 && $ch >= 'a' && $ch <= 'z') return $ch;
            if ($ch >= '0' && $ch <= '9') $size = intdiv($size, ord($ch) - 48);
            else $size--;
        }
        return "";
    }
}
