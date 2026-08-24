<?php
// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution {
    /**
     * @param String $encodedText
     * @param Integer $rows
     * @return String
     */
    function decodeCiphertext($encodedText, $rows) {
        if ($rows === 1) return $encodedText;
        $cols = intdiv(strlen($encodedText), $rows);
        $b = "";
        for ($c = 0; $c < $cols; $c++)
            for ($r = 0; $r < $rows && $c + $r < $cols; $r++)
                $b .= $encodedText[$r * $cols + $c + $r];
        return rtrim($b, ' ');
    }
}
