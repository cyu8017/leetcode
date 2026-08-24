<?php
// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

class Solution {
    public $s;
    public $n;
    public $memo;
    function minimumSubstringsInPartition($s) {
        $this->s = $s;
        $this->n = strlen($s);
        $this->memo = array_fill(0, $this->n, -1);
        return $this->dfs(0);
    }
    function dfs($i) {
        $n = $this->n;
        if ($i >= $n) return 0;
        if ($this->memo[$i] !== -1) return $this->memo[$i];
        $cnt = array_fill(0, 26, 0);
        $freq = [];
        $this->memo[$i] = $n - $i;
        for ($j = $i; $j < $n; $j++) {
            $k = ord($this->s[$j]) - 97;
            if ($cnt[$k] > 0) {
                $c = $cnt[$k];
                $nv = $freq[$c] - 1;
                if ($nv === 0) unset($freq[$c]);
                else $freq[$c] = $nv;
            }
            $cnt[$k]++;
            $freq[$cnt[$k]] = ($freq[$cnt[$k]] ?? 0) + 1;
            if (count($freq) === 1) {
                $this->memo[$i] = min($this->memo[$i], 1 + $this->dfs($j + 1));
            }
        }
        return $this->memo[$i];
    }
}
