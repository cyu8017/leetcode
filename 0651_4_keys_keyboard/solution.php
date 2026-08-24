<?php
// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

class Solution {
    function maxA($n) {
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 0; $i <= $n; ++$i) $dp[$i] = $i;
        for ($i = 1; $i <= $n; ++$i) {
            for ($j = 0; $j < $i - 2; ++$j) {
                $dp[$i] = max($dp[$i], $dp[$j] * ($i - $j - 1));
            }
        }
        return $dp[$n];
    }
}
