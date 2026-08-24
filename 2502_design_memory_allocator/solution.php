<?php
// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

class Allocator {
    private $mem;

    function __construct($n) {
        $this->mem = array_fill(0, $n, 0);
    }

    function allocate($size, $mID) {
        $freeCnt = 0;
        $len = count($this->mem);
        for ($i = 0; $i < $len; $i++) {
            if ($this->mem[$i] === 0) {
                $freeCnt++;
                if ($freeCnt === $size) {
                    $start = $i - $size + 1;
                    for ($j = $start; $j <= $i; $j++) $this->mem[$j] = $mID;
                    return $start;
                }
            } else $freeCnt = 0;
        }
        return -1;
    }

    function freeMemory($mID) {
        $cnt = 0;
        $len = count($this->mem);
        for ($i = 0; $i < $len; $i++) {
            if ($this->mem[$i] === $mID) {
                $this->mem[$i] = 0;
                $cnt++;
            }
        }
        return $cnt;
    }
}
