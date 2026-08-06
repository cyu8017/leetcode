<?php
// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

class FizzBuzz {
    private $n;
    private $current = 1;

    function __construct($n) {
        $this->n = $n;
    }

    function fizz($printFizz) {
        $this->run(fn($x) => $x % 3 === 0 && $x % 5 !== 0, $printFizz);
    }

    function buzz($printBuzz) {
        $this->run(fn($x) => $x % 5 === 0 && $x % 3 !== 0, $printBuzz);
    }

    function fizzbuzz($printFizzBuzz) {
        $this->run(fn($x) => $x % 15 === 0, $printFizzBuzz);
    }

    function number($printNumber) {
        $this->run(fn($x) => $x % 3 !== 0 && $x % 5 !== 0, function () use ($printNumber) {
            $printNumber($this->current);
        });
    }

    private function run($predicate, $action) {
        while ($this->current <= $this->n) {
            if ($predicate($this->current)) {
                $action();
                $this->current++;
            } else {
                usleep(100);
            }
        }
    }
}
