<?php
// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

class Solution {
    function nthSmallest($n, $k) {
        $MX = 50;
        $C = [];
        for ($i = 0; $i < $MX; $i++) $C[$i] = array_fill(0, $MX + 1, 0);
        for ($i = 0; $i < $MX; $i++) {
            $C[$i][0] = 1;
            for ($j = 1; $j <= $i; $j++) $C[$i][$j] = $C[$i - 1][$j - 1] + $C[$i - 1][$j];
        }
        $ans = 0;
        $nn = $n;
        for ($i = 49; $i >= 0; $i--) {
            if ($k >= 0 && $nn > $C[$i][$k]) {
                $nn -= $C[$i][$k];
                $ans |= 1 << $i;
                $k--;
                if ($k === 0) break;
            }
        }
        return $ans;
    }
}
