<?php
// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

class Solution {
    /**
     * @param String $num
     * @return String
     */
    function toHexspeak($num) {
        $value = (int)$num;
        $digits = '0123456789ABCDEF';
        $out = '';
        while ($value) {
            $rem = $value % 16;
            $value = intdiv($value, 16);
            if ($rem >= 2 && $rem <= 9) return 'ERROR';
            $out = $digits[$rem] . $out;
        }
        if ($out === '') $out = '0';
        return str_replace(['0', '1'], ['O', 'I'], $out);
    }
}
