<?php
// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

class Solution {
    private $s;
    private $limit;

    private function count($num) {
        if ($num < 0) return 0;
        $s = $this->s;
        $limit = $this->limit;
        for ($i = 0; $i < strlen($s); $i++) if (ord($s[$i]) - 48 > $limit) return 0;
        $t = (string)$num;
        $n = strlen($t);
        $sn = strlen($s);
        if ($n < $sn) return 0;
        $ans = 0;
        for ($length = $sn; $length < $n; $length++) {
            $preLen = $length - $sn;
            if ($preLen === 0) $ans += 1;
            else {
                $ways = $limit;
                for ($i = 1; $i < $preLen; $i++) $ways *= ($limit + 1);
                $ans += $ways;
            }
        }
        $pref = $n - $sn;
        $memo = [];
        $dfs = function($i, $tight) use (&$dfs, &$memo, $t, $pref, $s, $limit) {
            if ($i === $pref) {
                if ($tight) return substr($t, $pref) >= $s ? 1 : 0;
                return 1;
            }
            $key = ($i << 1) | ($tight ? 1 : 0);
            if (isset($memo[$key])) return $memo[$key];
            $up = $tight ? ord($t[$i]) - 48 : $limit;
            if ($up > $limit) $up = $limit;
            $res = 0;
            for ($d = 0; $d <= $up; $d++) {
                if ($i === 0 && $d === 0) continue;
                $res += $dfs($i + 1, $tight && $d === (ord($t[$i]) - 48));
            }
            $memo[$key] = $res;
            return $res;
        };
        $ans += $dfs(0, true);
        return $ans;
    }

    function numberOfPowerfulInt($start, $finish, $limit, $s) {
        $this->s = $s;
        $this->limit = $limit;
        return $this->count($finish) - $this->count($start - 1);
    }
}
