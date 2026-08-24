<?php
// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

class Solution {
    function nextDay($date) {
        $d = new DateTime($date);
        $d->modify('+1 day');
        return $d->format('Y-m-d');
    }
}
