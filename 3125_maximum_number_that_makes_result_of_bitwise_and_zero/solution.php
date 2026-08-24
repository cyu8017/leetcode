<?php
// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

class Solution {
    function maxNumber($n) {
        $len = 0;
        $x = $n;
        while ($x > 0) { $len++; $x >>= 1; }
        return (1 << ($len - 1)) - 1;
    }
}
