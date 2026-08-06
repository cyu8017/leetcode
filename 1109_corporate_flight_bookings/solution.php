<?php
// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

class Solution {
    /**
     * @param Integer[][] $bookings
     * @param Integer $n
     * @return Integer[]
     */
    function corpFlightBookings($bookings, $n) {
        $diff = array_fill(0, $n + 1, 0);
        foreach ($bookings as [$first, $last, $seats]) {
            $diff[$first - 1] += $seats;
            $diff[$last] -= $seats;
        }
        $ans = [];
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $ans[] = $cur;
        }
        return $ans;
    }
}
