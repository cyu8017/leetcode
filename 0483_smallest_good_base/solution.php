<?php
// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

class Solution {
    /**
     * @param string $n
     * @return string
     */
    function smallestGoodBase($n) {
        return $this->smallest_good_base($n);
    }

    /**
     * @param string $n
     * @return string
     */
    function smallest_good_base($n) {
        $num = (int)$n;
        $maxLength = (int)floor(log($num, 2)) + 1;
        for ($length = $maxLength; $length >= 2; $length--) {
            $low = 2;
            $high = $num - 1;
            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                $total = 1;
                $power = 1;
                $ok = true;
                for ($step = 0; $step < $length - 1; $step++) {
                    $power *= $mid;
                    $total += $power;
                    if ($total > $num) {
                        $ok = false;
                        break;
                    }
                }
                if ($ok && $total === $num) {
                    return (string)$mid;
                }
                if (!$ok || $total > $num) {
                    $high = $mid - 1;
                } else {
                    $low = $mid + 1;
                }
            }
        }
        return (string)($num - 1);
    }
}
