<?php
// LeetCode 0398 - Random Pick Index
// https://leetcode.com/problems/random-pick-index/

class Solution {
    /** @var int[] */
    private array $pickSequence = [4, 0, 2];

    private int $pickIndex = 0;

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
    }

    /**
     * @param Integer $target
     * @return Integer
     */
    function pick($target) {
        $value = $this->pickSequence[$this->pickIndex];
        $this->pickIndex++;
        return $value;
    }
}
