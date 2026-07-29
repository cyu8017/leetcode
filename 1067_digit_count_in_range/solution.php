<?php
// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

class Solution {
    /**
     * @param Integer $d
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function digitsCount($d, $low, $high) {
        $countUpto = function ($n) use ($d) {
            if ($n < 0) {
                return 0;
            }
            $s = (string)$n;
            $length = strlen($s);
            $ans = 0;
            for ($i = 0; $i < $length; $i++) {
                $left = $i ? (int)substr($s, 0, $i) : 0;
                $right = $i + 1 < $length ? (int)substr($s, $i + 1) : 0;
                $digit = (int)$s[$i];
                $power = 10 ** ($length - $i - 1);
                if ($d !== 0) {
                    $ans += $left * $power;
                    if ($digit > $d) {
                        $ans += $power;
                    } elseif ($digit === $d) {
                        $ans += $right + 1;
                    }
                } else {
                    if ($i === 0) {
                        continue;
                    }
                    $ans += ($left - 1) * $power;
                    if ($digit > 0) {
                        $ans += $power;
                    } else {
                        $ans += $right + 1;
                    }
                }
            }
            return $ans;
        };
        return $countUpto($high) - $countUpto($low - 1);
    }
}
