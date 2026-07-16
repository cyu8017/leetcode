<?php
// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

class Solution {
    /**
     * @param string $s
     * @return string
     */
    function encode($s) {
        $length = strlen($s);
        $dp = array_fill(0, $length + 1, "");

        $encodeWord = function ($word) {
            $size = strlen($word);
            $best = $word;
            for ($unitLength = 1; $unitLength <= intdiv($size, 2); $unitLength++) {
                if ($size % $unitLength !== 0) {
                    continue;
                }
                $unit = substr($word, 0, $unitLength);
                if (str_repeat($unit, intdiv($size, $unitLength)) === $word) {
                    $encoded = intdiv($size, $unitLength) . "[$unit]";
                    if (strlen($encoded) < strlen($best) || (strlen($encoded) === strlen($best) && $encoded < $best)) {
                        $best = $encoded;
                    }
                }
            }
            return $best;
        };

        for ($index = 1; $index <= $length; $index++) {
            $dp[$index] = $encodeWord(substr($s, 0, $index));
            for ($split = 1; $split < $index; $split++) {
                $candidate = $dp[$index - $split] . $encodeWord(substr($s, $index - $split, $split));
                if (strlen($candidate) < strlen($dp[$index]) || (strlen($candidate) === strlen($dp[$index]) && $candidate < $dp[$index])) {
                    $dp[$index] = $candidate;
                }
            }
        }
        return $dp[$length];
    }
}
