<?php
// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

class Street {
    public $doors;
    public $i = 0;
    function __construct($doors) {
        $this->doors = $doors;
    }
    function closeDoor() { $this->doors[$this->i] = 0; }
    function isDoorOpen() { return $this->doors[$this->i] == 1; }
    function moveRight() { $this->i = ($this->i + 1) % count($this->doors); }
}

class Solution {
    function houseCount($street, $k) {
        if (is_array($street)) $street = new Street($street);
        while (!$street->isDoorOpen()) $street->moveRight();
        $street->closeDoor();
        $street->moveRight();
        $ans = 1;
        for ($i = 1; $i < $k; $i++) {
            if ($street->isDoorOpen()) {
                $street->closeDoor();
                $ans = 0;
            }
            $ans++;
            $street->moveRight();
        }
        return $ans;
    }
}
