<?php
// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minMovesToMakePalindrome($s) {
        $b = str_split($s);
        $ans = 0;
        while (count($b) > 1) {
            $j = count($b) - 1;
            while ($j > 0 && $b[$j] !== $b[0]) $j--;
            if ($j === 0) {
                $ans += intdiv(count($b), 2);
                array_shift($b);
                $b = array_values($b);
                continue;
            }
            $ans += count($b) - 1 - $j;
            array_splice($b, $j, 1);
            array_shift($b);
            $b = array_values($b);
        }
        return $ans;
    }
}
