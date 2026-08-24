<?php
// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree {
    private $delta = [];

    function __construct() {
        $this->delta = [];
    }

    function book($startTime, $endTime) {
        $this->delta[$startTime] = ($this->delta[$startTime] ?? 0) + 1;
        $this->delta[$endTime] = ($this->delta[$endTime] ?? 0) - 1;
        $current = 0;
        $best = 0;
        $keys = array_keys($this->delta);
        sort($keys);
        foreach ($keys as $key) {
            $current += $this->delta[$key];
            $best = max($best, $current);
        }
        return $best;
    }
}
