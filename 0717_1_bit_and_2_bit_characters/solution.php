<?php
// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution {
    function isOneBitCharacter($bits) {
        $i = 0;
        $n = count($bits);
        while ($i < $n - 1) $i += $bits[$i] === 1 ? 2 : 1;
        return $i === $n - 1;
    }
}
