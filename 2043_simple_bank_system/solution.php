<?php
// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank {
    private $bal = [];

    /**
     * @param Integer[] $balance
     */
    function __construct($balance) {
        $this->bal = $balance;
    }

    private function valid($account) {
        return $account >= 1 && $account <= count($this->bal);
    }

    /**
     * @param Integer $account1
     * @param Integer $account2
     * @param Integer $money
     * @return Boolean
     */
    function transfer($account1, $account2, $money) {
        if (!$this->valid($account1) || !$this->valid($account2) || $this->bal[$account1 - 1] < $money) return false;
        $this->bal[$account1 - 1] -= $money;
        $this->bal[$account2 - 1] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function deposit($account, $money) {
        if (!$this->valid($account)) return false;
        $this->bal[$account - 1] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function withdraw($account, $money) {
        if (!$this->valid($account) || $this->bal[$account - 1] < $money) return false;
        $this->bal[$account - 1] -= $money;
        return true;
    }
}
