<?php
// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

class Solution {
    function powm($a, $e, $mod) {
        $res = 1;
        while ($e > 0) {
            if (($e & 1) !== 0) $res = $res * $a % $mod;
            $a = $a * $a % $mod;
            $e >>= 1;
        }
        return $res;
    }
    function zigZagArrays($n, $l, $r) {
        $mod = 1000000007;
        $points = $n + 1;
        $values = array_fill(0, $points + 1, 0);
        for ($m = 1; $m <= $points; $m++) {
            $up = [];
            $down = [];
            for ($value = 0; $value < $m; $value++) {
                $up[$value] = $value;
                $down[$value] = $m - 1 - $value;
            }
            for ($length = 3; $length <= $n; $length++) {
                $nextUp = array_fill(0, $m, 0);
                $nextDown = array_fill(0, $m, 0);
                $prefix = 0;
                for ($value = 0; $value < $m; $value++) {
                    $nextUp[$value] = $prefix;
                    $prefix = ($prefix + $down[$value]) % $mod;
                }
                $suffix = 0;
                for ($value = $m - 1; $value >= 0; $value--) {
                    $nextDown[$value] = $suffix;
                    $suffix = ($suffix + $up[$value]) % $mod;
                }
                $up = $nextUp;
                $down = $nextDown;
            }
            for ($value = 0; $value < $m; $value++) {
                $values[$m] = ($values[$m] + $up[$value] + $down[$value]) % $mod;
            }
        }
        $x = ($r - $l + 1) % $mod;
        if ($r - $l + 1 <= $points) return $values[$r - $l + 1];
        $prefixA = [];
        $suffixA = [];
        $prefixA[0] = 1;
        for ($i = 1; $i <= $points; $i++) {
            $prefixA[$i] = $prefixA[$i - 1] * (($x - $i + $mod) % $mod) % $mod;
        }
        $suffixA[$points + 1] = 1;
        for ($i = $points; $i >= 1; $i--) {
            $suffixA[$i] = $suffixA[$i + 1] * (($x - $i + $mod) % $mod) % $mod;
        }
        $factorial = [];
        $factorial[0] = 1;
        for ($i = 1; $i <= $points; $i++) $factorial[$i] = $factorial[$i - 1] * $i % $mod;
        $answer = 0;
        for ($i = 1; $i <= $points; $i++) {
            $numerator = $prefixA[$i - 1] * $suffixA[$i + 1] % $mod;
            $denominator = $factorial[$i - 1] * $factorial[$points - $i] % $mod;
            $term = $values[$i] * $numerator % $mod * $this->powm($denominator, $mod - 2, $mod) % $mod;
            if (($points - $i) % 2 === 1) $answer -= $term;
            else $answer += $term;
            $answer %= $mod;
        }
        if ($answer < 0) $answer += $mod;
        return $answer;
    }
}
