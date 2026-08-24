<?php
// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution {
    /**
     * @param int $n
     * @param int $k
     * @return int
     */
    function findKthNumber($n, $k) {
        return $this->find_kth_number($n, $k);
    }

    /**
     * @param int $n
     * @param int $k
     * @return int
     */
    function find_kth_number($n, $k) {
        $current = 1;
        $k--;

        while ($k > 0) {
            $steps = $this->countSteps($n, $current, $current + 1);
            if ($steps <= $k) {
                $current++;
                $k -= $steps;
            } else {
                $current *= 10;
                $k--;
            }
        }

        return $current;
    }

    private function countSteps(int $n, int $first, int $last): int {
        $steps = 0;
        while ($first <= $n) {
            $steps += min($n + 1, $last) - $first;
            $first *= 10;
            $last *= 10;
        }
        return $steps;
    }
}
