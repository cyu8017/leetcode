<?php
// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

class ATM {
    private $cnt;
    private $vals;

    function __construct() {
        $this->cnt = [0, 0, 0, 0, 0];
        $this->vals = [20, 50, 100, 200, 500];
    }

    function deposit($banknotesCount) {
        for ($i = 0; $i < 5; $i++) $this->cnt[$i] += $banknotesCount[$i];
    }

    function withdraw($amount) {
        $take = [0, 0, 0, 0, 0];
        $remain = $amount;
        $tmp = $this->cnt;
        for ($i = 4; $i >= 0; $i--) {
            $need = intdiv($remain, $this->vals[$i]);
            if ($need > $tmp[$i]) $need = $tmp[$i];
            $take[$i] = $need;
            $remain -= $need * $this->vals[$i];
        }
        if ($remain !== 0) return [-1];
        for ($i = 0; $i < 5; $i++) $this->cnt[$i] -= $take[$i];
        return $take;
    }
}
