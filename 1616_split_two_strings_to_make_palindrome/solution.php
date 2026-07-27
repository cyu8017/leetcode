<?php
// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution {
    private function isPal($s, $i, $j) {
        while ($i < $j) {
            if ($s[$i] !== $s[$j]) {
                return false;
            }
            $i++;
            $j--;
        }
        return true;
    }

    private function check($x, $y) {
        $i = 0;
        $j = strlen($x) - 1;
        while ($i < $j && $x[$i] === $y[$j]) {
            $i++;
            $j--;
        }
        return $this->isPal($x, $i, $j) || $this->isPal($y, $i, $j);
    }

    /**
     * @param String $a
     * @param String $b
     * @return Boolean
     */
    function checkPalindromeFormation($a, $b) {
        return $this->check($a, $b) || $this->check($b, $a);
    }
}
