<?php
// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

class Solution {
    function getEncryptedString($s, $k) {
        $n = strlen($s);
        $out = '';
        for ($i = 0; $i < $n; $i++) $out .= $s[($i + $k) % $n];
        return $out;
    }
}
