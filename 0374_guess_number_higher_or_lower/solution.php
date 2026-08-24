<?php
// LeetCode 0374 - Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/

function guess($num) {
    global $pick;
    if ($num > $pick) {
        return -1;
    }
    if ($num < $pick) {
        return 1;
    }
    return 0;
}

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function guessNumber($n) {
        return $this->guess_number($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function guess_number($n) {
        $left = 1;
        $right = $n;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            $result = guess($mid);
            if ($result === 0) {
                return $mid;
            }
            if ($result < 0) {
                $right = $mid - 1;
            } else {
                $left = $mid + 1;
            }
        }

        return $left;
    }
}
