<?php
// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countNicePairs($nums) {
        $mod = 1000000007;
        $freq = [];
        $ans = 0;

        foreach ($nums as $num) {
            $diff = $num - $this->rev($num);
            $ans = ($ans + ($freq[$diff] ?? 0)) % $mod;
            $freq[$diff] = ($freq[$diff] ?? 0) + 1;
        }

        return $ans;
    }

    /**
     * @param int $x
     * @return int
     */
    private function rev($x) {
        return (int)strrev((string)$x);
    }
}
