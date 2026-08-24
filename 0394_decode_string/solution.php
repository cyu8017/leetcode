<?php
// LeetCode 0394 - Decode String
// https://leetcode.com/problems/decode-string/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function decodeString($s) {
        return $this->decode_string($s);
    }

    /**
     * @param String $s
     * @return String
     */
    function decode_string($s) {
        $stack = [];
        $current = "";
        $number = 0;
        $length = strlen($s);

        for ($index = 0; $index < $length; $index++) {
            $char = $s[$index];
            if ($char >= "0" && $char <= "9") {
                $number = $number * 10 + (int)$char;
            } elseif ($char === "[") {
                $stack[] = [$current, $number];
                $current = "";
                $number = 0;
            } elseif ($char === "]") {
                [$previous, $count] = array_pop($stack);
                $current = $previous . str_repeat($current, $count);
            } else {
                $current .= $char;
            }
        }

        return $current;
    }
}
