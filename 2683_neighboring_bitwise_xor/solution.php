<?php
// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
    function doesValidArrayExist($derived) {
        $x = 0;
        foreach ($derived as $v) $x ^= $v;
        return $x === 0;
    }
}
