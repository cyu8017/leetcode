<?php
// LeetCode 3758 - Convert Number Words to Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

class Solution {
    function convertNumber($s) {
        $d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
        $n = strlen($s);
        $ans = '';
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < 10; $j++) {
                $m = strlen($d[$j]);
                if ($i + $m <= $n && substr($s, $i, $m) === $d[$j]) {
                    $ans .= chr(48 + $j);
                    $i += $m - 1;
                    break;
                }
            }
        }
        return $ans;
    }
}
