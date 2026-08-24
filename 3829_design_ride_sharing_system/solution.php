<?php
// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem {
    public $t = 0;
    public $riders = [];
    public $drivers = [];
    public $d = [];
    public $riderKeys = [];
    public $driverKeys = [];
    function __construct() {
        $this->t = 0;
        $this->riders = [];
        $this->drivers = [];
        $this->d = [];
        $this->riderKeys = [];
        $this->driverKeys = [];
    }
    function addRider($riderId) {
        $this->d[$riderId] = $this->t;
        $this->riders[$this->t] = $riderId;
        $this->riderKeys[] = $this->t;
        $this->t++;
    }
    function addDriver($driverId) {
        $this->drivers[$this->t] = $driverId;
        $this->driverKeys[] = $this->t;
        $this->t++;
    }
    function matchDriverWithRider() {
        while (count($this->riderKeys) && !isset($this->riders[$this->riderKeys[0]])) array_shift($this->riderKeys);
        while (count($this->driverKeys) && !isset($this->drivers[$this->driverKeys[0]])) array_shift($this->driverKeys);
        if (!count($this->riderKeys) || !count($this->driverKeys)) return [-1, -1];
        $dKey = array_shift($this->driverKeys);
        $rKey = array_shift($this->riderKeys);
        $driverId = $this->drivers[$dKey];
        $riderId = $this->riders[$rKey];
        unset($this->drivers[$dKey]);
        unset($this->riders[$rKey]);
        return [$driverId, $riderId];
    }
    function cancelRider($riderId) {
        if (!isset($this->d[$riderId])) return;
        unset($this->riders[$this->d[$riderId]]);
    }
}
