<?php
// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findNumbers($nums) {
        $ans = 0;
        foreach ($nums as $value) {
            if (strlen((string)$value) % 2 === 0) $ans++;
        }
        return $ans;
    }
}
