<?php

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function getLengthOfOptimalCompression($s, $k) {
        $n = strlen($s);
        $memo = [];
        $dp = function ($index, $remaining) use (&$dp, &$memo, $s, $n) {
            if ($remaining < 0) {
                return 1000000000;
            }
            if ($index === $n || $n - $index <= $remaining) {
                return 0;
            }
            $key = $index . ',' . $remaining;
            if (isset($memo[$key])) {
                return $memo[$key];
            }
            $answer = $dp($index + 1, $remaining - 1);
            $same = 0;
            $removed = 0;
            for ($j = $index; $j < $n; $j++) {
                if ($s[$j] === $s[$index]) {
                    $same++;
                    $encoded = 1 + ($same >= 2 ? 1 : 0) + ($same >= 10 ? 1 : 0) + ($same >= 100 ? 1 : 0);
                    $answer = min($answer, $encoded + $dp($j + 1, $remaining - $removed));
                } else {
                    $removed++;
                    if ($removed > $remaining) {
                        break;
                    }
                }
            }
            return $memo[$key] = $answer;
        };
        return $dp(0, $k);
    }
}
