<?php
// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

class Solution {
    function minimizeXor($num1, $num2) {
        $bits = 0;
        for ($x = $num2; $x !== 0; $x &= $x - 1) $bits++;
        $ans = 0;
        for ($i = 31; $i >= 0 && $bits > 0; $i--) {
            if ((($num1 >> $i) & 1) !== 0) {
                $ans |= 1 << $i;
                $bits--;
            }
        }
        for ($i = 0; $i < 32 && $bits > 0; $i++) {
            if ((($ans >> $i) & 1) === 0) {
                $ans |= 1 << $i;
                $bits--;
            }
        }
        return $ans;
    }
}
