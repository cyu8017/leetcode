<?php
// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow {
    private $n;
    private $m;
    private $sum;
    private $mx;

    function __construct($n, $m) {
        $this->n = $n;
        $this->m = $m;
        $this->sum = array_fill(0, 4 * $n, 0);
        $this->mx = array_fill(0, 4 * $n, 0);
        $this->build(1, 0, $n - 1);
    }

    private function pull($idx) {
        $this->sum[$idx] = $this->sum[$idx * 2] + $this->sum[$idx * 2 + 1];
        $this->mx[$idx] = max($this->mx[$idx * 2], $this->mx[$idx * 2 + 1]);
    }

    private function build($idx, $l, $r) {
        if ($l === $r) {
            $this->sum[$idx] = $this->mx[$idx] = $this->m;
            return;
        }
        $mid = ($l + $r) >> 1;
        $this->build($idx * 2, $l, $mid);
        $this->build($idx * 2 + 1, $mid + 1, $r);
        $this->pull($idx);
    }

    private function update($idx, $l, $r, $pos, $val) {
        if ($l === $r) {
            $this->sum[$idx] = $this->mx[$idx] = $val;
            return;
        }
        $mid = ($l + $r) >> 1;
        if ($pos <= $mid) $this->update($idx * 2, $l, $mid, $pos, $val);
        else $this->update($idx * 2 + 1, $mid + 1, $r, $pos, $val);
        $this->pull($idx);
    }

    private function querySum($idx, $l, $r, $ql, $qr) {
        if ($qr < $l || $r < $ql) return 0;
        if ($ql <= $l && $r <= $qr) return $this->sum[$idx];
        $mid = ($l + $r) >> 1;
        return $this->querySum($idx * 2, $l, $mid, $ql, $qr) + $this->querySum($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
    }

    private function findFirst($idx, $l, $r, $maxRow, $k) {
        if ($l > $maxRow || $this->mx[$idx] < $k) return -1;
        if ($l === $r) return $l;
        $mid = ($l + $r) >> 1;
        $left = $this->findFirst($idx * 2, $l, $mid, $maxRow, $k);
        if ($left !== -1) return $left;
        return $this->findFirst($idx * 2 + 1, $mid + 1, $r, $maxRow, $k);
    }

    function gather($k, $maxRow) {
        $row = $this->findFirst(1, 0, $this->n - 1, $maxRow, $k);
        if ($row === -1) return [];
        $remain = $this->querySum(1, 0, $this->n - 1, $row, $row);
        $seat = $this->m - $remain;
        $this->update(1, 0, $this->n - 1, $row, $remain - $k);
        return [$row, $seat];
    }

    function scatter($k, $maxRow) {
        if ($this->querySum(1, 0, $this->n - 1, 0, $maxRow) < $k) return false;
        $need = $k;
        for ($row = 0; $row <= $maxRow && $need > 0; $row++) {
            $remain = $this->querySum(1, 0, $this->n - 1, $row, $row);
            if ($remain === 0) continue;
            $take = min($remain, $need);
            $this->update(1, 0, $this->n - 1, $row, $remain - $take);
            $need -= $take;
        }
        return true;
    }
}
