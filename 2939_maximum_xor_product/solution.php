<?php
// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

class Solution {
    function maximumXorProduct($a, $b, $n) {
        $mod = 1000000007;
        $A = $a;
        $B = $b;
        for ($i = $n - 1; $i >= 0; $i--) {
            $bit = 1 << $i;
            $abit = $A & $bit;
            $bbit = $B & $bit;
            if ($abit === $bbit) {
                $A |= $bit;
                $B |= $bit;
            } else if ($A > $B) {
                $B |= $bit;
                $A &= ~$bit;
            } else {
                $A |= $bit;
                $B &= ~$bit;
            }
        }
        return (int)(($A % $mod) * ($B % $mod) % $mod);
    }
}
