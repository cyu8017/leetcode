<?php
// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

class Solution {
    public $s;
    public $memo;
    function countSteppingNumbers($low, $high) {
        $MOD = 1000000007;
        $dec = function($s) {
            $arr = str_split($s);
            $i = count($arr) - 1;
            while ($i >= 0 && $arr[$i] === '0') {
                $arr[$i] = '9';
                $i--;
            }
            if ($i >= 0) $arr[$i] = chr(ord($arr[$i]) - 1);
            $j = 0;
            while ($j < count($arr) - 1 && $arr[$j] === '0') $j++;
            return implode('', array_slice($arr, $j));
        };
        $ans = ($this->countTo($high) - $this->countTo($dec($low))) % $MOD;
        if ($ans < 0) $ans += $MOD;
        return $ans;
    }
    function countTo($s) {
        $this->s = $s;
        $this->memo = [];
        return $this->dfs(0, 1, -1, 0);
    }
    function dfs($pos, $tight, $last, $started) {
        $MOD = 1000000007;
        if ($pos === strlen($this->s)) return $started;
        $key = $pos . ',' . $tight . ',' . $last . ',' . $started;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $up = $tight ? ord($this->s[$pos]) - 48 : 9;
        $ans = 0;
        for ($d = 0; $d <= $up; $d++) {
            $nt = ($tight && $d === $up) ? 1 : 0;
            if (!$started) {
                if ($d === 0) $ans += $this->dfs($pos + 1, $nt, -1, 0);
                else $ans += $this->dfs($pos + 1, $nt, $d, 1);
            } else if (abs($d - $last) === 1) {
                $ans += $this->dfs($pos + 1, $nt, $d, 1);
            }
        }
        return $this->memo[$key] = $ans % $MOD;
    }
}
