<?php
// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

class ParkingSystem {
    private $spaces;

    /**
     * @param Integer $big
     * @param Integer $medium
     * @param Integer $small
     */
    function __construct($big, $medium, $small) {
        $this->spaces = [0, $big, $medium, $small];
    }

    /**
     * @param Integer $carType
     * @return Boolean
     */
    function addCar($carType) {
        if ($this->spaces[$carType] === 0) {
            return false;
        }
        $this->spaces[$carType]--;
        return true;
    }
}
