<?php
// LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

class Solution {
    function maximumXor($s, $t) {
        $cnt = [0, 0];
        $nt = strlen($t);
        for ($i = 0; $i < $nt; $i++) $cnt[ord($t[$i]) - 48]++;
        $n = strlen($s);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $x = ord($s[$i]) - 48;
            if ($cnt[$x ^ 1] > 0) {
                $cnt[$x ^ 1]--;
                $ans[$i] = '1';
            } else {
                $cnt[$x]--;
                $ans[$i] = '0';
            }
        }
        return implode('', $ans);
    }
}
