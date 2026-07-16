<?php
// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

class Solution {
    /**
     * @param int $n
     * @return int
     */
    function largestPalindrome($n) {
        return $this->largest_palindrome($n);
    }

    /**
     * @param int $n
     * @return int
     */
    function largest_palindrome($n) {
        if ($n === 1) {
            return 9;
        }
        $upper = 10 ** $n - 1;
        $lower = 10 ** ($n - 1);
        for ($first = $upper; $first >= $lower; $first--) {
            $candidate = (int)($first . strrev((string)$first));
            for ($factor = $upper; $factor * $factor >= $candidate; $factor--) {
                if ($candidate % $factor === 0) {
                    $partner = intdiv($candidate, $factor);
                    if ($partner >= $lower && $partner <= $upper) {
                        return $candidate % 1337;
                    }
                }
            }
        }
        return 0;
    }
}
