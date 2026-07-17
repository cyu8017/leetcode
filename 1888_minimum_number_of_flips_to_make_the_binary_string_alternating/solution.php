<?php
// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minFlips($s) {
        $n = strlen($s);
        $doubled = $s . $s;
        $alt0 = 0;
        $alt1 = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($doubled[$i] !== ($i % 2 === 0 ? '0' : '1')) {
                $alt0++;
            }
            if ($doubled[$i] !== ($i % 2 === 0 ? '1' : '0')) {
                $alt1++;
            }
        }

        $answer = min($alt0, $alt1);
        for ($i = 0; $i < $n; $i++) {
            if ($doubled[$i] !== ($i % 2 === 0 ? '0' : '1')) {
                $alt0--;
            }
            if ($doubled[$i + $n] !== (($i + $n) % 2 === 0 ? '0' : '1')) {
                $alt0++;
            }

            if ($doubled[$i] !== ($i % 2 === 0 ? '1' : '0')) {
                $alt1--;
            }
            if ($doubled[$i + $n] !== (($i + $n) % 2 === 0 ? '1' : '0')) {
                $alt1++;
            }

            $answer = min($answer, $alt0, $alt1);
        }

        return $answer;
    }
}
