<?php
// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

class Solution {
    function rob($nums) {
        $n = count($nums);
        if ($n === 1) {
            return $nums[0];
        }
        return max(
            $this->robLinear(array_slice($nums, 0, $n - 1)),
            $this->robLinear(array_slice($nums, 1))
        );
    }

    private function robLinear($houses) {
        $prev2 = 0;
        $prev1 = 0;
        foreach ($houses as $num) {
            $temp = max($prev1, $prev2 + $num);
            $prev2 = $prev1;
            $prev1 = $temp;
        }
        return $prev1;
    }
}
