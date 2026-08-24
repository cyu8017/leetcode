<?php
// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

class Solution {
    function partitionString($s) {
        $ans = 1;
        $seen = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $bit = 1 << (ord($s[$i]) - 97);
            if (($seen & $bit) !== 0) {
                $ans++;
                $seen = 0;
            }
            $seen |= $bit;
        }
        return $ans;
    }
}
