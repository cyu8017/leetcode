<?php
// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

class Solution {
    function countDivisibleSubstrings($word) {
        $vals = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9];
        $ans = 0;
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $sum = 0;
            for ($j = $i; $j < $n; $j++) {
                $sum += $vals[ord($word[$j]) - 97];
                if ($sum % ($j - $i + 1) === 0) $ans++;
            }
        }
        return $ans;
    }
}
