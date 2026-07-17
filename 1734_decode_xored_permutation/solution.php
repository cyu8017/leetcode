<?php
// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

class Solution {
    /**
     * @param Integer[] $encoded
     * @return Integer[]
     */
    function decode($encoded) {
        $n = count($encoded) + 1;
        $total = 0;
        for ($value = 1; $value <= $n; $value++) {
            $total ^= $value;
        }
        $odd = 0;
        for ($i = 1; $i < count($encoded); $i += 2) {
            $odd ^= $encoded[$i];
        }
        $ans = [$total ^ $odd];
        foreach ($encoded as $value) {
            $ans[] = $ans[count($ans) - 1] ^ $value;
        }
        return $ans;
    }
}
