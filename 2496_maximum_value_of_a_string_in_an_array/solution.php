<?php
// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution {
    function maximumValue($strs) {
        $ans = 0;
        foreach ($strs as $s) {
            $allDigit = true;
            $val = 0;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $c = $s[$i];
                if ($c < '0' || $c > '9') { $allDigit = false; break; }
                $val = $val * 10 + (ord($c) - 48);
            }
            if (!$allDigit) $val = $len;
            if ($val > $ans) $ans = $val;
        }
        return $ans;
    }
}
