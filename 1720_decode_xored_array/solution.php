<?php
// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

class Solution {
    /**
     * @param Integer[] $encoded
     * @param Integer $first
     * @return Integer[]
     */
    function decode($encoded, $first) {
        $ans = [$first];
        foreach ($encoded as $value) {
            $ans[] = end($ans) ^ $value;
        }
        return $ans;
    }
}
