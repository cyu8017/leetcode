<?php
// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream {
    private $value;
    private $k;
    private $streak;

    function __construct($value, $k) {
        $this->value = $value;
        $this->k = $k;
        $this->streak = 0;
    }

    function consec($num) {
        if ($num === $this->value) $this->streak++;
        else $this->streak = 0;
        return $this->streak >= $this->k;
    }
}
