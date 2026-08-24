<?php
// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution {
    function sumOfEncryptedInt($nums) {
        $ans = 0;
        foreach ($nums as $x) $ans += $this->encrypt($x);
        return $ans;
    }
    function encrypt($x) {
        $mx = 0;
        $p = 0;
        for (; $x > 0; $x = intdiv($x, 10)) {
            $mx = max($mx, $x % 10);
            $p = $p * 10 + 1;
        }
        return $mx * $p;
    }
}
