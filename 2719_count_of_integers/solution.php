<?php
// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

class Solution {
    function count($num1, $num2, $min_sum, $max_sum) {
        $MOD = 1000000007;
        $dec = function($s) {
            $arr = str_split($s);
            $i = count($arr) - 1;
            while ($i >= 0 && $arr[$i] === "0") { $arr[$i] = "9"; $i--; }
            if ($i >= 0) $arr[$i] = chr(ord($arr[$i]) - 1);
            $j = 0;
            while ($j < count($arr) - 1 && $arr[$j] === "0") $j++;
            return implode("", array_slice($arr, $j));
        };
        $dp = function($s) use ($min_sum, $max_sum, $MOD) {
            $memo = [];
            $dfs = function($pos, $sum, $tight) use (&$dfs, &$memo, $s, $min_sum, $max_sum, $MOD) {
                if ($sum > $max_sum) return 0;
                if ($pos === strlen($s)) return $sum >= $min_sum ? 1 : 0;
                $key = $pos . "," . $sum . "," . ($tight ? 1 : 0);
                if (isset($memo[$key])) return $memo[$key];
                $up = $tight ? ord($s[$pos]) - 48 : 9;
                $res = 0;
                for ($d = 0; $d <= $up; $d++) {
                    $res = ($res + $dfs($pos + 1, $sum + $d, $tight && $d === $up)) % $MOD;
                }
                $memo[$key] = $res;
                return $res;
            };
            return $dfs(0, 0, true);
        };
        return ($dp($num2) - $dp($dec($num1)) + $MOD) % $MOD;
    }
}
