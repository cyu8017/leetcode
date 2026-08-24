<?php
// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution {
    /**
     * @param Integer $num
     * @return Integer
     */
    function countEven($num) {
        $ans = 0;
        for ($x = 1; $x <= $num; $x++) {
            $s = 0;
            $y = $x;
            while ($y > 0) { $s += $y % 10; $y = intdiv($y, 10); }
            if ($s % 2 === 0) $ans++;
        }
        return $ans;
    }
}
