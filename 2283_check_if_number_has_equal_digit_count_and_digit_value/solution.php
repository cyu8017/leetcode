<?php
// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution {
    function digitCount($num) {
        $cnt = array_fill(0, 10, 0);
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) $cnt[ord($num[$i]) - 48]++;
        for ($i = 0; $i < $n; $i++)
            if ($cnt[$i] !== ord($num[$i]) - 48) return false;
        return true;
    }
}
