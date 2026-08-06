<?php

class Solution {
    private $memo = [];

    /**
     * @param Integer $n
     * @return Integer
     */
    function minDays($n) {
        $this->memo = [];
        return $this->dp($n);
    }

    private function dp($x) {
        if ($x <= 1) {
            return $x;
        }
        if (isset($this->memo[$x])) {
            return $this->memo[$x];
        }
        $result = 1 + min(
            ($x % 2) + $this->dp(intdiv($x, 2)),
            ($x % 3) + $this->dp(intdiv($x, 3))
        );
        $this->memo[$x] = $result;
        return $result;
    }
}
