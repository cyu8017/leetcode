<?php
// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

class Solution {
    function toLowerCase($s) {
        $chars = str_split($s);
        $n = count($chars);
        for ($i = 0; $i < $n; $i++) {
            $code = ord($chars[$i]);
            if ($code >= 65 && $code <= 90) $chars[$i] = chr($code + 32);
        }
        return implode('', $chars);
    }
}
