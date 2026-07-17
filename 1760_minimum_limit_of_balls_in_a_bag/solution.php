<?php
// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $maxOperations
     * @return Integer
     */
    function minimumSize($nums, $maxOperations) {
        $lo = 1;
        $hi = max($nums);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $ops = 0;
            foreach ($nums as $x) {
                $ops += intdiv($x - 1, $mid);
            }
            if ($ops <= $maxOperations) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }
        return $lo;
    }
}
