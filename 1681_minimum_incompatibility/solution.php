<?php
// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

class Solution {
    private $memo = [];
    private $groups = [];
    private $n;
    private $full;

    function minimumIncompatibility($nums, $k) {
        $this->n = count($nums);
        $size = intdiv($this->n, $k);
        $this->full = (1 << $this->n) - 1;
        $this->groups = [];
        for ($mask = 0; $mask < (1 << $this->n); $mask++) {
            if ($this->popcount($mask) !== $size) continue;
            $vals = [];
            for ($i = 0; $i < $this->n; $i++) {
                if (($mask >> $i) & 1) $vals[] = $nums[$i];
            }
            if (count(array_unique($vals)) === $size) {
                $this->groups[$mask] = max($vals) - min($vals);
            }
        }
        $this->memo = [];
        $ans = $this->dp(0);
        return $ans >= 1000000000 ? -1 : $ans;
    }

    private function popcount($x) {
        $c = 0;
        while ($x) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    private function dp($mask) {
        if ($mask === $this->full) return 0;
        if (isset($this->memo[$mask])) return $this->memo[$mask];
        $first = 0;
        while (($mask >> $first) & 1) $first++;
        $best = 1000000000;
        foreach ($this->groups as $g => $c) {
            if ((($g >> $first) & 1) && !($g & $mask)) {
                $best = min($best, $c + $this->dp($mask | $g));
            }
        }
        return $this->memo[$mask] = $best;
    }
}
