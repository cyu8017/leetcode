<?php

// LeetCode 0191 - Number of 1 Bits
class Solution {
    function hammingWeight($n) {
        $count = 0;
        while ($n != 0) {
            $n &= $n - 1;
            $count++;
        }
        return $count;
    }
}