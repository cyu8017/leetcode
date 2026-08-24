<?php
// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest {
    private $k;
    private $heap = [];

    function __construct($k, $nums) {
        $this->k = $k;
        foreach ($nums as $num) $this->add($num);
    }

    function add($val) {
        $this->heap[] = $val;
        sort($this->heap);
        if (count($this->heap) > $this->k) array_shift($this->heap);
        return $this->heap[0];
    }
}
