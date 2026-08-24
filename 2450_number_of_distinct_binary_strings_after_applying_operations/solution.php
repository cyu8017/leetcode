<?php
// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

class Solution {
    function countDistinctStrings($s, $k) {
        $mod = 1000000007;
        $n = strlen($s);
        $ans = 1;
        for ($i = 0; $i < $n - $k + 1; $i++) $ans = ($ans * 2) % $mod;
        return $ans;
    }
}
