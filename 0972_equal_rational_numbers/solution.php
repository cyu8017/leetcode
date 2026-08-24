<?php
// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

class Solution {
    function isRationalEqual($s, $t) {
        $parse = function ($x) {
            if (strpos($x, "(") === false) return $x === "" ? 0.0 : (float)$x;
            $lp = strpos($x, "(");
            $nonRep = substr($x, 0, $lp);
            $rep = substr($x, $lp + 1, -1);
            if (strpos($nonRep, ".") === false) $nonRep .= ".";
            $dot = strpos($nonRep, ".");
            $integer = substr($nonRep, 0, $dot);
            $frac = substr($nonRep, $dot + 1);
            $bas = $integer === "" ? 0.0 : (float)$integer;
            if (strlen($frac) > 0) {
                $denom = 1;
                for ($i = 0; $i < strlen($frac); $i++) $denom *= 10;
                $bas += (float)$frac / $denom;
            }
            if (strlen($rep) > 0) {
                $repVal = (float)$rep;
                $cycle = 1;
                for ($i = 0; $i < strlen($rep); $i++) $cycle *= 10;
                $denom = $cycle - 1;
                for ($i = 0; $i < strlen($frac); $i++) $denom *= 10;
                $bas += $repVal / $denom;
            }
            return $bas;
        };
        return abs($parse($s) - $parse($t)) < 1e-12;
    }
}
