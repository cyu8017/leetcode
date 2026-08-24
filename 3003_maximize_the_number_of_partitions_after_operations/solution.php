<?php
// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

class Solution {
    private $s;
    private $n;
    private $k;
    private $memo;

    private function popcount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    private function dfs($i, $cur, $t) {
        if ($i >= $this->n) return 1;
        $kkey = $i . '|' . $cur . '|' . $t;
        if (isset($this->memo[$kkey])) return $this->memo[$kkey];
        $v = 1 << (ord($this->s[$i]) - 97);
        $nxt = $cur | $v;
        if ($this->popcount($nxt) > $this->k) $ans = $this->dfs($i + 1, $v, $t) + 1;
        else $ans = $this->dfs($i + 1, $nxt, $t);
        if ($t > 0) {
            for ($j = 0; $j < 26; $j++) {
                $nxt = $cur | (1 << $j);
                if ($this->popcount($nxt) > $this->k)
                    $ans = max($ans, $this->dfs($i + 1, 1 << $j, 0) + 1);
                else
                    $ans = max($ans, $this->dfs($i + 1, $nxt, 0));
            }
        }
        $this->memo[$kkey] = $ans;
        return $ans;
    }

    function maxPartitionsAfterOperations($s, $k) {
        $this->s = $s;
        $this->n = strlen($s);
        $this->k = $k;
        $this->memo = [];
        return $this->dfs(0, 0, 1);
    }
}
