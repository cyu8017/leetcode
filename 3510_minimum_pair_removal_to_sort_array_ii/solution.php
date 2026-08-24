<?php
// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

class Solution {
    private $sl;
    private $slMap;

    private function key($sum, $i) {
        return $sum * 1000000007 + $i;
    }

    private function addSl($sum, $i) {
        $k = $this->key($sum, $i);
        $this->slMap[$k] = [$sum, $i];
        $lo = 0;
        $hi = count($this->sl);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->sl[$mid][0] < $sum || ($this->sl[$mid][0] === $sum && $this->sl[$mid][1] < $i)) $lo = $mid + 1;
            else $hi = $mid;
        }
        array_splice($this->sl, $lo, 0, [[$sum, $i]]);
    }

    private function remSl($sum, $i) {
        $k = $this->key($sum, $i);
        if (!isset($this->slMap[$k])) return;
        unset($this->slMap[$k]);
        $n = count($this->sl);
        for ($t = 0; $t < $n; $t++) {
            if ($this->sl[$t][0] === $sum && $this->sl[$t][1] === $i) {
                array_splice($this->sl, $t, 1);
                break;
            }
        }
    }

    private function ceiling($idx, $x) {
        $best = null;
        foreach ($idx as $v => $_) {
            if ($v >= $x && ($best === null || $v < $best)) $best = $v;
        }
        return $best;
    }

    private function floorIdx($idx, $x) {
        $best = null;
        foreach ($idx as $v => $_) {
            if ($v <= $x && ($best === null || $v > $best)) $best = $v;
        }
        return $best;
    }

    function minimumPairRemoval($nums) {
        $n = count($nums);
        $inv = 0;
        $ans = 0;
        $this->sl = [];
        $this->slMap = [];
        $idx = [];
        for ($i = 0; $i < $n; $i++) $idx[$i] = true;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] > $nums[$i + 1]) $inv++;
            $this->addSl($nums[$i] + $nums[$i + 1], $i);
        }
        while ($inv > 0) {
            $ans++;
            $p = array_shift($this->sl);
            unset($this->slMap[$this->key($p[0], $p[1])]);
            $s = $p[0];
            $i = $p[1];
            $j = $this->ceiling($idx, $i + 1);
            if ($nums[$i] > $nums[$j]) $inv--;
            $h = $this->floorIdx($idx, $i - 1);
            if ($h !== null) {
                if ($nums[$h] > $nums[$i]) $inv--;
                $this->remSl($nums[$h] + $nums[$i], $h);
                if ($nums[$h] > $s) $inv++;
                $this->addSl($nums[$h] + $s, $h);
            }
            $kk = $this->ceiling($idx, $j + 1);
            if ($kk !== null) {
                if ($nums[$j] > $nums[$kk]) $inv--;
                $this->remSl($nums[$j] + $nums[$kk], $j);
                if ($s > $nums[$kk]) $inv++;
                $this->addSl($s + $nums[$kk], $i);
            }
            $nums[$i] = $s;
            unset($idx[$j]);
        }
        return $ans;
    }
}
