<?php
// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

class SeatManager {
    /** @var SplMinHeap */
    private $available;

    /**
     * @param Integer $n
     */
    function __construct($n) {
        $this->available = new SplMinHeap();
        for ($i = 1; $i <= $n; $i++) {
            $this->available->insert($i);
        }
    }

    /**
     * @return Integer
     */
    function reserve() {
        return $this->available->extract();
    }

    /**
     * @param Integer $seatNumber
     * @return NULL
     */
    function unreserve($seatNumber) {
        $this->available->insert($seatNumber);
    }
}
