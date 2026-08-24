<?php
// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution {
    function removeAlmostEqualCharacters($word) {
        $ans = 0;
        $i = 1;
        $n = strlen($word);
        while ($i < $n) {
            if (abs(ord($word[$i]) - ord($word[$i - 1])) <= 1) {
                $ans++;
                $i += 2;
            } else $i++;
        }
        return $ans;
    }
}
