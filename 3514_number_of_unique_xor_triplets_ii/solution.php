<?php
// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

class Solution {
    function uniqueXorTriplets($nums) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        $mx <<= 1;
        $st = array_fill(0, $mx, false);
        foreach ($nums as $a)
            foreach ($nums as $b) $st[$a ^ $b] = true;
        $s = array_fill(0, $mx, 0);
        for ($ab = 0; $ab < $mx; $ab++) {
            if ($st[$ab]) foreach ($nums as $c) $s[$ab ^ $c] = 1;
        }
        $ans = 0;
        foreach ($s as $v) $ans += $v;
        return $ans;
    }
}
