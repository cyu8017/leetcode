<?php
// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

class Street {
    public $doors;
    public $i = 0;
    function __construct($doors) {
        $this->doors = $doors;
    }
    function closeDoor() { $this->doors[$this->i] = 0; }
    function openDoor() { $this->doors[$this->i] = 1; }
    function isDoorOpen() { return $this->doors[$this->i] == 1; }
    function moveRight() { $this->i = ($this->i + 1) % count($this->doors); }
}

class Solution {
    function houseCount($street, $k) {
        if (is_array($street)) $street = new Street($street);
        for ($i = 0; $i < $k; $i++) {
            $street->closeDoor();
            $street->moveRight();
        }
        $ans = 0;
        for (;;) {
            $ans++;
            $street->openDoor();
            $street->moveRight();
            if ($street->isDoorOpen()) break;
        }
        return $ans;
    }
}
