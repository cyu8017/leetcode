<?php
// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

class Solution {
    private $dem;
    private $n;
    private $memo;
    private $W;
    private $bestServe;

    function minMaxWaitingTime($demand, $fuel) {
        $this->dem = $demand;
        $this->n = count($demand);
        $f0 = $fuel[0];
        $f1 = $fuel[1];
        if ($f0 < $demand[0] && $f1 < $demand[0]) return -1;
        $this->memo = [];
        $this->bestServe = $this->maxServe(0, $f0, $f1, 0, 0);
        if ($this->bestServe == 0) return -1;
        $lo = 0;
        $hi = 0;
        foreach ($demand as $x) $hi += $x;
        $ans = $hi;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $this->W = $mid;
            $this->memo = [];
            if ($this->canWithW(0, $f0, $f1, 0, 0)) {
                $ans = $mid;
                $hi = $mid - 1;
            } else {
                $lo = $mid + 1;
            }
        }
        return $ans;
    }

    private function packKey($i, $f0, $f1, $d0, $d1) {
        return (((($i * 51 + $f0) * 51 + $f1) * 21 + $d0) * 21 + $d1);
    }

    private function maxServe($i, $f0, $f1, $d0, $d1) {
        if ($i == $this->n) return $i;
        $key = $this->packKey($i, $f0, $f1, $d0, $d1);
        if (isset($this->memo[$key])) return $this->memo[$key];
        $need = $this->dem[$i];
        $can0 = $f0 >= $need;
        $can1 = $f1 >= $need;
        $best = $i;
        if (!$can0 && !$can1) {
            $this->memo[$key] = $best;
            return $best;
        }
        if ($can0) {
            $nd1 = $d1 > $d0 ? $d1 - $d0 : 0;
            $best = max($best, $this->maxServe($i + 1, $f0 - $need, $f1, $need, $nd1));
        }
        if ($can1) {
            $nd0 = $d0 > $d1 ? $d0 - $d1 : 0;
            $best = max($best, $this->maxServe($i + 1, $f0, $f1 - $need, $nd0, $need));
        }
        $this->memo[$key] = $best;
        return $best;
    }

    private function canWithW($i, $f0, $f1, $d0, $d1) {
        if ($i >= $this->bestServe) return true;
        if ($i == $this->n) return true;
        $key = $this->packKey($i, $f0, $f1, $d0, $d1);
        if (isset($this->memo[$key])) return $this->memo[$key] == 2;
        $need = $this->dem[$i];
        $can0 = $f0 >= $need;
        $can1 = $f1 >= $need;
        $ok = false;
        if (!$can0 && !$can1) {
            $this->memo[$key] = 1;
            return false;
        }
        if ($can0 && $d0 <= $this->W) {
            $nd1 = $d1 > $d0 ? $d1 - $d0 : 0;
            if ($this->canWithW($i + 1, $f0 - $need, $f1, $need, $nd1)) $ok = true;
        }
        if (!$ok && $can1 && $d1 <= $this->W) {
            $nd0 = $d0 > $d1 ? $d0 - $d1 : 0;
            if ($this->canWithW($i + 1, $f0, $f1 - $need, $nd0, $need)) $ok = true;
        }
        $this->memo[$key] = $ok ? 2 : 1;
        return $ok;
    }
}
