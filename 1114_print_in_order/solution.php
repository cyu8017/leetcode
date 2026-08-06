<?php
// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

class Foo {
    private $secondReady = false;
    private $thirdReady = false;

    function first($printFirst) {
        $printFirst();
        $this->secondReady = true;
    }

    function second($printSecond) {
        while (!$this->secondReady) { usleep(100); }
        $printSecond();
        $this->thirdReady = true;
    }

    function third($printThird) {
        while (!$this->thirdReady) { usleep(100); }
        $printThird();
    }
}
