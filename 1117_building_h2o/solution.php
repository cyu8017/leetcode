<?php
// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

class H2O {
    private $h = 0;
    private $o = 0;

    function hydrogen($releaseHydrogen) {
        while (true) {
            if ($this->h < 2) {
                $this->h++;
                $releaseHydrogen();
                $this->maybeReset();
                return;
            }
            usleep(100);
        }
    }

    function oxygen($releaseOxygen) {
        while (true) {
            if ($this->o < 1) {
                $this->o++;
                $releaseOxygen();
                $this->maybeReset();
                return;
            }
            usleep(100);
        }
    }

    private function maybeReset() {
        if ($this->h === 2 && $this->o === 1) {
            $this->h = 0;
            $this->o = 0;
        }
    }
}
