<?php
// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

class Solution {
    function evenNumberBitwiseORs($nums) {
        $ans = 0;
        foreach ($nums as $x) if ($x % 2 === 0) $ans |= $x;
        return $ans;
    }
}
