<?php
// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

class MKAverage {
    /** @var int */
    private $m;
    /** @var int */
    private $k;
    /** @var int[] */
    private $stream = [];

    /**
     * @param Integer $m
     * @param Integer $k
     */
    function __construct($m, $k) {
        $this->m = $m;
        $this->k = $k;
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function addElement($num) {
        $this->stream[] = $num;
    }

    /**
     * @return Integer
     */
    function calculateMKAverage() {
        if (count($this->stream) < $this->m) {
            return -1;
        }
        $window = array_slice($this->stream, -$this->m);
        sort($window);
        $middle = array_slice($window, $this->k, count($window) - 2 * $this->k);
        return intdiv(array_sum($middle), count($middle));
    }
}
