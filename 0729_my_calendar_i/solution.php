<?php
// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

class MyCalendar {
    private $bookings = [];

    function __construct() {
        $this->bookings = [];
    }

    function book($startTime, $endTime) {
        foreach ($this->bookings as $b) {
            if ($b[0] < $endTime && $startTime < $b[1]) return false;
        }
        $this->bookings[] = [$startTime, $endTime];
        return true;
    }
}
