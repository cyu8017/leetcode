<?php
// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

class DiningPhilosophers {
    private $forks;

    function __construct() {
        $this->forks = array_fill(0, 5, false);
    }

    /**
     * @param Integer $philosopher
     * @param Callable $pickLeftFork
     * @param Callable $pickRightFork
     * @param Callable $eat
     * @param Callable $putLeftFork
     * @param Callable $putRightFork
     * @return NULL
     */
    function wantsToEat($philosopher, $pickLeftFork, $pickRightFork, $eat, $putLeftFork, $putRightFork) {
        $left = $philosopher;
        $right = ($philosopher + 1) % 5;
        if ($philosopher % 2 === 0) {
            $first = $left; $second = $right;
        } else {
            $first = $right; $second = $left;
        }
        while ($this->forks[$first]) { usleep(100); }
        $this->forks[$first] = true;
        while ($this->forks[$second]) { usleep(100); }
        $this->forks[$second] = true;
        $pickLeftFork();
        $pickRightFork();
        $eat();
        $putLeftFork();
        $putRightFork();
        $this->forks[$first] = false;
        $this->forks[$second] = false;
    }
}
