<?php
// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo {
    private $booked = [];
    private $overlaps = [];

    function __construct() {
        $this->booked = [];
        $this->overlaps = [];
    }

    function book($startTime, $endTime) {
        foreach ($this->overlaps as $o) {
            if ($o[0] < $endTime && $startTime < $o[1]) return false;
        }
        foreach ($this->booked as $b) {
            if ($b[0] < $endTime && $startTime < $b[1]) {
                $this->overlaps[] = [max($b[0], $startTime), min($b[1], $endTime)];
            }
        }
        $this->booked[] = [$startTime, $endTime];
        return true;
    }
}
