<?php
// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

class FooBar {
    private $n;
    private $fooTurn = true;

    function __construct($n) {
        $this->n = $n;
    }

    function foo($printFoo) {
        for ($i = 0; $i < $this->n; $i++) {
            while (!$this->fooTurn) { usleep(100); }
            $printFoo();
            $this->fooTurn = false;
        }
    }

    function bar($printBar) {
        for ($i = 0; $i < $this->n; $i++) {
            while ($this->fooTurn) { usleep(100); }
            $printBar();
            $this->fooTurn = true;
        }
    }
}
