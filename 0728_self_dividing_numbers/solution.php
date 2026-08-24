<?php
// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

class Solution {
    function selfDividingNumbers($left, $right) {
        $isSelfDividing = function ($num) {
            $x = $num;
            while ($x > 0) {
                $digit = $x % 10;
                if ($digit === 0 || $num % $digit !== 0) return false;
                $x = intdiv($x, 10);
            }
            return true;
        };
        $result = [];
        for ($num = $left; $num <= $right; $num++) if ($isSelfDividing($num)) $result[] = $num;
        return $result;
    }
}
