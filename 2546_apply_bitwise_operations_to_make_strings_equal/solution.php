<?php
// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution {
    function makeStringsEqual($s, $target) {
        $has1s = false;
        $has1t = false;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '1') $has1s = true;
            if ($target[$i] === '1') $has1t = true;
        }
        return $has1s === $has1t;
    }
}
