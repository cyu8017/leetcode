<?php
// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

class ZeroEvenOdd {
    private $n;
    private $state = 0; // 0=zero, 1=odd, 2=even
    private $x = 1;

    function __construct($n) {
        $this->n = $n;
    }

    function zero($printNumber) {
        for ($i = 0; $i < $this->n; $i++) {
            while ($this->state !== 0) { usleep(100); }
            $printNumber(0);
            $this->state = ($this->x % 2 === 1) ? 1 : 2;
        }
    }

    function even($printNumber) {
        for ($i = 2; $i <= $this->n; $i += 2) {
            while ($this->state !== 2) { usleep(100); }
            $printNumber($i);
            $this->x++;
            $this->state = 0;
        }
    }

    function odd($printNumber) {
        for ($i = 1; $i <= $this->n; $i += 2) {
            while ($this->state !== 1) { usleep(100); }
            $printNumber($i);
            $this->x++;
            $this->state = 0;
        }
    }
}
