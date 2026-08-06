<?php
// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

class TrafficLight {
    private $greenRoad = 1;

    function __construct() {}

    /**
     * @param Integer $carId
     * @param Integer $roadId
     * @param Integer $direction
     * @param Callable $turnGreen
     * @param Callable $crossCar
     * @return NULL
     */
    function carArrived($carId, $roadId, $direction, $turnGreen, $crossCar) {
        if ($roadId !== $this->greenRoad) {
            $turnGreen();
            $this->greenRoad = $roadId;
        }
        $crossCar();
    }
}
