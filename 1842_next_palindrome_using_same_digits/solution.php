<?php
// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

class Solution {
    /**
     * @param String $num
     * @return String
     */
    function nextPalindrome($num) {
        $nums = str_split($num);

        if (!$this->nextPermutation($nums)) {
            return "";
        }

        $n = count($nums);
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            $nums[$n - $i - 1] = $nums[$i];
        }
        return implode("", $nums);
    }

    /**
     * @param string[] $nums
     * @return bool
     */
    private function nextPermutation(&$nums) {
        $n = intdiv(count($nums), 2);
        $i = $n - 2;
        while ($i >= 0 && $nums[$i] >= $nums[$i + 1]) {
            $i--;
        }
        if ($i < 0) {
            return false;
        }

        $j = $n - 1;
        while ($nums[$j] <= $nums[$i]) {
            $j--;
        }
        [$nums[$i], $nums[$j]] = [$nums[$j], $nums[$i]];
        $left = $i + 1;
        $right = $n - 1;
        while ($left < $right) {
            [$nums[$left], $nums[$right]] = [$nums[$right], $nums[$left]];
            $left++;
            $right--;
        }
        return true;
    }
}
