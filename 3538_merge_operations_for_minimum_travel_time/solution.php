<?php
// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

class Solution {
    private $n;
    private $prefix;
    private $position;
    private $memo;
    private $INF = 1e18;

    private function dp($i, $skips, $last) {
        if ($i === $this->n - 1) return $skips === 0 ? 0 : $this->INF;
        $key = $i . ',' . $skips . ',' . $last;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $rate = $this->prefix[$i];
        if ($last > 0) $rate -= $this->prefix[$last - 1];
        $res = $this->INF;
        $end = $this->n - 1;
        if ($i + $skips + 1 < $end) $end = $i + $skips + 1;
        for ($j = $i + 1; $j <= $end; $j++) {
            $cand = ($this->position[$j] - $this->position[$i]) * $rate + $this->dp($j, $skips - ($j - $i - 1), $i + 1);
            if ($cand < $res) $res = $cand;
        }
        return $this->memo[$key] = $res;
    }

    function minTravelTime($l, $n, $k, $position, $time) {
        $this->n = $n;
        $this->position = $position;
        $this->prefix = array_fill(0, $n, 0);
        $this->prefix[0] = $time[0];
        for ($i = 1; $i < $n; $i++) $this->prefix[$i] = $this->prefix[$i - 1] + $time[$i];
        $this->memo = [];
        return $this->dp(0, $k, 0);
    }
}
