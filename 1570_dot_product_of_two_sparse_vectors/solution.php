<?php

class SparseVector {
    public $values = [];

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        foreach ($nums as $i => $x) {
            if ($x) {
                $this->values[$i] = $x;
            }
        }
    }

    /**
     * Return the dotProduct of two sparse vectors
     * @param SparseVector $vec
     * @return Integer
     */
    function dotProduct($vec) {
        if (count($this->values) > count($vec->values)) {
            return $vec->dotProduct($this);
        }
        $sum = 0;
        foreach ($this->values as $i => $x) {
            if (isset($vec->values[$i])) {
                $sum += $x * $vec->values[$i];
            }
        }
        return $sum;
    }
}

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function dotProduct($nums1, $nums2) {
        return (new SparseVector($nums1))->dotProduct(new SparseVector($nums2));
    }
}
