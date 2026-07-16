<?php

// LeetCode 0231 - Power of Two
// https://leetcode.com/problems/power-of-two/

class Solution {
    function isPowerOfTwo($n) {
        return $n > 0 && ($n & ($n - 1)) === 0;
    }
}
