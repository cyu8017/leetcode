<?php

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function longestAwesome($s) {
        $first = [0 => -1];
        $mask = 0;
        $answer = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $mask ^= 1 << intval($s[$i]);
            if (array_key_exists($mask, $first)) {
                $answer = max($answer, $i - $first[$mask]);
            } else {
                $first[$mask] = $i;
            }
            for ($bit = 0; $bit < 10; $bit++) {
                $candidate = $mask ^ (1 << $bit);
                if (array_key_exists($candidate, $first)) {
                    $answer = max($answer, $i - $first[$candidate]);
                }
            }
        }
        return $answer;
    }
}
