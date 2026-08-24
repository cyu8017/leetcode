<?php
// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function minSteps($s, $t) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $n = strlen($t);
        for ($i = 0; $i < $n; $i++) $freq[ord($t[$i]) - 97]--;
        $ans = 0;
        foreach ($freq as $v) $ans += abs($v);
        return $ans;
    }
}
