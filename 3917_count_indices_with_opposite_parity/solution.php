<?php
// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

class Solution {
    function countOppositeParity($nums) {
        $cnt = [0, 0];
        foreach ($nums as $x) $cnt[$x & 1]++;
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $cnt[$x & 1]--;
            $ans[$i] = $cnt[($x & 1) ^ 1];
        }
        return $ans;
    }
}
