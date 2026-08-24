<?php
// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

class Solution {
    function shortestMatchingSubstring($s, $p) {
        $parts = [];
        $cur = "";
        $plen = strlen($p);
        for ($i = 0; $i < $plen; $i++) {
            $c = $p[$i];
            if ($c === "*") {
                $parts[] = $cur;
                $cur = "";
            } else $cur .= $c;
        }
        $parts[] = $cur;
        while (count($parts) < 3) $parts[] = "";
        $a = $parts[0];
        $b = $parts[1];
        $c = $parts[2];
        $n = strlen($s);
        $findAll = function($sub) use ($s, $n) {
            $res = [];
            $slen = strlen($sub);
            if ($slen === 0) {
                for ($i = 0; $i <= $n; $i++) $res[] = $i;
                return $res;
            }
            for ($i = 0; $i + $slen <= $n; $i++) {
                if (substr($s, $i, $slen) === $sub) $res[] = $i;
            }
            return $res;
        };
        $sortSearch = function($arr, $x) {
            $lo = 0;
            $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $posA = $findAll($a);
        $posB = $findAll($b);
        $posC = $findAll($c);
        $ans = $n + 1;
        $alen = strlen($a);
        $blen = strlen($b);
        $clen = strlen($c);
        foreach ($posA as $ia) {
            $endA = $ia + $alen;
            $bi = $sortSearch($posB, $endA);
            for (; $bi < count($posB); $bi++) {
                $endB = $posB[$bi] + $blen;
                $ci = $sortSearch($posC, $endB);
                if ($ci < count($posC)) {
                    $length = $posC[$ci] + $clen - $ia;
                    if ($length < $ans) $ans = $length;
                }
                break;
            }
        }
        return $ans === $n + 1 ? -1 : $ans;
    }
}
