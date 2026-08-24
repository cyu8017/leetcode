<?php
// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution {
    function atMostNGivenDigitSet($digits, $n) {
        $k = count($digits);
        $ipow = function ($bas, $exp) {
            $r = 1;
            while ($exp-- > 0) $r *= $bas;
            return $r;
        };
        $countUpTo = function ($t) use (&$countUpTo, $digits, $k, $ipow) {
            if ($t === "") return 0;
            $first = 0;
            foreach ($digits as $d) {
                if ($d[0] < $t[0]) $first++;
            }
            $ways = $first * $ipow($k, strlen($t) - 1);
            $found = false;
            foreach ($digits as $d) {
                if ($d[0] === $t[0]) {
                    $found = true;
                    break;
                }
            }
            if ($found) $ways += $countUpTo(substr($t, 1));
            return $ways;
        };
        $s = strval($n);
        $m = strlen($s);
        $ans = 0;
        for ($i = 1; $i < $m; $i++) $ans += $ipow($k, $i);
        $ans += $countUpTo($s);
        return $ans;
    }
}
