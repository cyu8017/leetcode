<?php
// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

class _ASHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp) { $this->cmp = $cmp; }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($cmp($a[$i], $a[$p]) >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i;
            $l = $i * 2 + 1;
            $r = $l + 1;
            if ($l < $n && $cmp($a[$l], $a[$s]) < 0) $s = $l;
            if ($r < $n && $cmp($a[$r], $a[$s]) < 0) $s = $r;
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!count($a)) return null;
        $top = $a[0];
        $last = array_pop($a);
        if (count($a)) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}

class AuctionSystem {
    public $bids;
    public $heaps;
    function __construct() {
        $this->bids = [];
        $this->heaps = [];
    }
    function addBid($userId, $itemId, $bidAmount) {
        if (!isset($this->bids[$itemId])) $this->bids[$itemId] = [];
        $this->bids[$itemId][$userId] = $bidAmount;
        if (!isset($this->heaps[$itemId])) {
            $this->heaps[$itemId] = new _ASHeap(function($a, $b) {
                if ($a['amount'] !== $b['amount']) return $b['amount'] - $a['amount'];
                return $b['userId'] - $a['userId'];
            });
        }
        $this->heaps[$itemId]->push(['amount' => $bidAmount, 'userId' => $userId]);
    }
    function updateBid($userId, $itemId, $newAmount) {
        $this->addBid($userId, $itemId, $newAmount);
    }
    function removeBid($userId, $itemId) {
        if (isset($this->bids[$itemId])) unset($this->bids[$itemId][$userId]);
    }
    function getHighestBidder($itemId) {
        if (!isset($this->heaps[$itemId])) return -1;
        $h = $this->heaps[$itemId];
        $m = isset($this->bids[$itemId]) ? $this->bids[$itemId] : [];
        while ($h->size()) {
            $top = $h->peek();
            if (isset($m[$top['userId']]) && $m[$top['userId']] === $top['amount']) return $top['userId'];
            $h->pop();
        }
        return -1;
    }
}
