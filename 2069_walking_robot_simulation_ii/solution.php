<?php
// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot {
    private $w;
    private $h;
    private $peri;
    private $pos = 0;
    private $moved = false;

    /**
     * @param Integer $width
     * @param Integer $height
     */
    function __construct($width, $height) {
        $this->w = $width;
        $this->h = $height;
        $this->peri = 2 * ($width + $height) - 4;
        $this->pos = 0;
        $this->moved = false;
    }

    private function getPosDir() {
        $p = $this->pos;
        if ($p === 0) {
            if (!$this->moved) return [0, 0, 0];
            return [0, 0, 3];
        }
        if ($p <= $this->w - 1) return [$p, 0, 0];
        $p -= $this->w - 1;
        if ($p <= $this->h - 1) return [$this->w - 1, $p, 1];
        $p -= $this->h - 1;
        if ($p <= $this->w - 1) return [$this->w - 1 - $p, $this->h - 1, 2];
        $p -= $this->w - 1;
        return [0, $this->h - 1 - $p, 3];
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function step($num) {
        $this->moved = true;
        $this->pos = ($this->pos + $num) % $this->peri;
    }

    /**
     * @return Integer[]
     */
    function getPos() {
        $pd = $this->getPosDir();
        return [$pd[0], $pd[1]];
    }

    /**
     * @return String
     */
    function getDir() {
        $names = ["East", "North", "West", "South"];
        return $names[$this->getPosDir()[2]];
    }
}
