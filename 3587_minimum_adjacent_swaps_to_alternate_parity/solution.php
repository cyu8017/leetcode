<?php
// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

class Solution {
    private function calc($pos, $n, $k) {
        $res = 0;
        for ($i = 0; $i < $n; $i += 2) $res += abs($pos[$k][intdiv($i, 2)] - $i);
        return $res;
    }

    function minSwaps($nums) {
        $pos = [[], []];
        for ($i = 0; $i < count($nums); $i++) $pos[$nums[$i] & 1][] = $i;
        if (abs(count($pos[0]) - count($pos[1])) > 1) return -1;
        if (count($pos[0]) > count($pos[1])) return $this->calc($pos, count($nums), 0);
        if (count($pos[0]) < count($pos[1])) return $this->calc($pos, count($nums), 1);
        return min($this->calc($pos, count($nums), 0), $this->calc($pos, count($nums), 1));
    }
}
