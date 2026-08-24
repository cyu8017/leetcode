<?php
// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution {
    private function f($x, $k) {
        $res = '';
        while ($x > 0) {
            $v = $x % $k;
            $res .= $v <= 9 ? chr(48 + $v) : chr(65 + $v - 10);
            $x = intdiv($x, $k);
        }
        return strrev($res);
    }

    function concatHex36($n) {
        return $this->f($n * $n, 16) . $this->f($n * $n * $n, 36);
    }
}
