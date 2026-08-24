<?php
// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter {
    private $q;

    function __construct() {
        $this->q = [];
    }

    function ping($t) {
        $this->q[] = $t;
        while ($this->q[0] < $t - 3000) array_shift($this->q);
        return count($this->q);
    }
}
