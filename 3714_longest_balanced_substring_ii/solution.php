<?php
// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

class Solution {
    function longestBalanced($s) {
        $calc1 = function($str) {
            $res = 0;
            $n = strlen($str);
            $i = 0;
            while ($i < $n) {
                $j = $i + 1;
                while ($j < $n && $str[$j] === $str[$i]) $j++;
                $res = max($res, $j - $i);
                $i = $j;
            }
            return $res;
        };
        $calc2 = function($str, $a, $b) {
            $res = 0;
            $n = strlen($str);
            $i = 0;
            while ($i < $n) {
                while ($i < $n && $str[$i] !== $a && $str[$i] !== $b) $i++;
                $pos = [];
                $pos[0] = $i - 1;
                $d = 0;
                while ($i < $n && ($str[$i] === $a || $str[$i] === $b)) {
                    if ($str[$i] === $a) $d++;
                    else $d--;
                    if (isset($pos[$d])) $res = max($res, $i - $pos[$d]);
                    else $pos[$d] = $i;
                    $i++;
                }
            }
            return $res;
        };
        $calc3 = function($str) {
            $pos = [];
            $pos['0,0'] = -1;
            $cnt = [0, 0, 0];
            $res = 0;
            $n = strlen($str);
            for ($i = 0; $i < $n; $i++) {
                $cnt[ord($str[$i]) - 97]++;
                $x = $cnt[0] - $cnt[1];
                $y = $cnt[1] - $cnt[2];
                $k = $x . ',' . $y;
                if (isset($pos[$k])) $res = max($res, $i - $pos[$k]);
                else $pos[$k] = $i;
            }
            return $res;
        };
        $x = $calc1($s);
        $y = max($calc2($s, 'a', 'b'), max($calc2($s, 'b', 'c'), $calc2($s, 'a', 'c')));
        $z = $calc3($s);
        return max($x, max($y, $z));
    }
}
