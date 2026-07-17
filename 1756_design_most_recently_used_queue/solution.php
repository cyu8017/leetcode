<?php
// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

class MRUQueue {
    private $q;

    /**
     * @param Integer $n
     */
    function __construct($n) {
        $this->q = range(1, $n);
    }

    /**
     * @param Integer $k
     * @return Integer
     */
    function fetch($k) {
        $val = $this->q[$k - 1];
        array_splice($this->q, $k - 1, 1);
        $this->q[] = $val;
        return $val;
    }
}
