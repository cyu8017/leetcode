<?php
// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution {
    function differenceOfSum($nums) {
        $elem = 0;
        $digit = 0;
        foreach ($nums as $num) {
            $elem += $num;
            $x = $num;
            while ($x > 0) {
                $digit += $x % 10;
                $x = intdiv($x, 10);
            }
        }
        return abs($elem - $digit);
    }
}
