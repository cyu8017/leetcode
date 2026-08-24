<?php
// LeetCode 0384 - Shuffle an Array
// https://leetcode.com/problems/shuffle-an-array/

class Solution {
    /** @var int[] */
    private array $original;

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->original = $nums;
        mt_srand(47);
    }

    /**
     * @return Integer[]
     */
    function reset() {
        return $this->original;
    }

    /**
     * @return Integer[]
     */
    function shuffle() {
        $result = $this->original;
        shuffle($result);
        return $result;
    }
}
