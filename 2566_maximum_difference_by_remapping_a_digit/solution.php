<?php
// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution {
    function minMaxDifference($num) {
        $s = (string)$num;
        $remap = function($from, $to) use ($s) {
            $v = 0;
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $d = $s[$i] === $from ? $to : $s[$i];
                $v = $v * 10 + (ord($d) - 48);
            }
            return $v;
        };
        $maxV = $num;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== '9') {
                $maxV = $remap($s[$i], '9');
                break;
            }
        }
        $minV = $remap($s[0], '0');
        return $maxV - $minV;
    }
}
