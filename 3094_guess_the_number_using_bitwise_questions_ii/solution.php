<?php
// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

function commonBits($num) {
    global $hiddenNumber;
    $hiddenNumber ^= $num;
    return substr_count(decbin($hiddenNumber), "1");
}

class Solution {
    function findNumber() {
        $n = 0;
        for ($i = 0; $i < 32; $i++) {
            $count1 = commonBits(1 << $i);
            $count2 = commonBits(1 << $i);
            if ($count1 > $count2) $n |= 1 << $i;
        }
        return $n;
    }
}
