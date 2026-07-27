<?php
// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue {
    private $l = [];
    private $r = [];

    function __construct() {
    }

    private function bal() {
        while (count($this->l) > count($this->r) + 1) {
            array_unshift($this->r, array_pop($this->l));
        }
        while (count($this->r) > count($this->l)) {
            $this->l[] = array_shift($this->r);
        }
    }

    function pushFront($val) {
        array_unshift($this->l, $val);
        $this->bal();
    }

    function pushMiddle($val) {
        if (count($this->l) > count($this->r)) {
            array_unshift($this->r, array_pop($this->l));
        }
        $this->l[] = $val;
    }

    function pushBack($val) {
        $this->r[] = $val;
        $this->bal();
    }

    function popFront() {
        if (!$this->l) return -1;
        $v = array_shift($this->l);
        $this->bal();
        return $v;
    }

    function popMiddle() {
        if (!$this->l) return -1;
        $v = array_pop($this->l);
        $this->bal();
        return $v;
    }

    function popBack() {
        if (!$this->l) return -1;
        $v = $this->r ? array_pop($this->r) : array_pop($this->l);
        $this->bal();
        return $v;
    }
}
