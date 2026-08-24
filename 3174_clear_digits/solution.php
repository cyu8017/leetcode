<?php
// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

class Solution {
    function clearDigits($s) {
        $stk = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c >= '0' && $c <= '9') array_pop($stk);
            else $stk[] = $c;
        }
        return implode('', $stk);
    }
}
