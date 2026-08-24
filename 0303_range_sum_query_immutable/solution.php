<?php
// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

class NumArray {
    /** @var int[] */
    private $prefix;

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->prefix = [0];
        foreach ($nums as $num) {
            $this->prefix[] = $this->prefix[count($this->prefix) - 1] + $num;
        }
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function sumRange($left, $right) {
        return $this->prefix[$right + 1] - $this->prefix[$left];
    }
}
