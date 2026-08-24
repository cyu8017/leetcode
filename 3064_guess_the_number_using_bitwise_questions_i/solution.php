<?php
// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

function commonSetBits($num) {
    global $hiddenNumber;
    return substr_count(decbin(($hiddenNumber ?? 0) & $num), "1");
}

class Solution {
    function findNumber() {
        $n = 0;
        for ($i = 0; $i < 32; $i++) {
            if (commonSetBits(1 << $i) > 0) $n |= 1 << $i;
        }
        return $n;
    }
}
