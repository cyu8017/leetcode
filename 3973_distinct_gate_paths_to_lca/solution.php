<?php
// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

class Solution {
    private $MOD = 1000000007;

    function gatePathXor($n, $parent, $gates, $queries) {
        $logn = 1;
        while ((1 << $logn) <= $n) $logn++;
        $up = array_fill(0, $logn, array_fill(0, $n, 0));
        $product = array_fill(0, $logn, array_fill(0, $n, null));
        $children = array_fill(0, $n, []);
        for ($node = 1; $node < $n; $node++) $children[$parent[$node]][] = $node;
        $depth = array_fill(0, $n, 0);
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($children[$u] as $v) {
                $depth[$v] = $depth[$u] + 1;
                $order[] = $v;
            }
        }
        for ($u = 0; $u < $n; $u++) {
            $up[0][$u] = ($u === 0) ? 0 : $parent[$u];
            $product[0][$u] = [
                [$gates[$u][1], $gates[$u][2]],
                [$gates[$u][2], $gates[$u][0]]
            ];
        }
        for ($level = 1; $level < $logn; $level++) {
            for ($u = 0; $u < $n; $u++) {
                $mid = $up[$level - 1][$u];
                $up[$level][$u] = $up[$level - 1][$mid];
                $product[$level][$u] = $this->multiply($product[$level - 1][$u], $product[$level - 1][$mid]);
            }
        }
        $answer = 0;
        foreach ($queries as $query) {
            $ancestor = $this->lca($query[0], $query[2], $depth, $up, $logn);
            $alice = $this->ways($query[0], $query[1], $depth[$query[0]] - $depth[$ancestor], $up, $product);
            $bob = $this->ways($query[2], $query[3], $depth[$query[2]] - $depth[$ancestor], $up, $product);
            $total = ($alice * $bob) % $this->MOD;
            $answer ^= $total;
        }
        return $answer;
    }

    private function multiply($a, $b) {
        $c = [[0, 0], [0, 0]];
        for ($i = 0; $i < 2; $i++) {
            for ($j = 0; $j < 2; $j++) {
                for ($k = 0; $k < 2; $k++) {
                    $c[$i][$j] = ($c[$i][$j] + $a[$i][$k] * $b[$k][$j]) % $this->MOD;
                }
            }
        }
        return $c;
    }

    private function liftNode($node, $distance, $up) {
        for ($level = 0; $distance > 0; $level++) {
            if (($distance & 1) !== 0) $node = $up[$level][$node];
            $distance >>= 1;
        }
        return $node;
    }

    private function lca($a, $b, $depth, $up, $logn) {
        if ($depth[$a] > $depth[$b]) $a = $this->liftNode($a, $depth[$a] - $depth[$b], $up);
        else if ($depth[$b] > $depth[$a]) $b = $this->liftNode($b, $depth[$b] - $depth[$a], $up);
        if ($a === $b) return $a;
        for ($level = $logn - 1; $level >= 0; $level--) {
            if ($up[$level][$a] !== $up[$level][$b]) {
                $a = $up[$level][$a];
                $b = $up[$level][$b];
            }
        }
        return $up[0][$a];
    }

    private function ways($node, $card, $distance, $up, $product) {
        $vector = [0, 0];
        $vector[$card] = 1;
        for ($level = 0; $distance > 0; $level++) {
            if (($distance & 1) !== 0) {
                $matrix = $product[$level][$node];
                $vector = [
                    ($vector[0] * $matrix[0][0] + $vector[1] * $matrix[1][0]) % $this->MOD,
                    ($vector[0] * $matrix[0][1] + $vector[1] * $matrix[1][1]) % $this->MOD
                ];
                $node = $up[$level][$node];
            }
            $distance >>= 1;
        }
        return ($vector[0] + $vector[1]) % $this->MOD;
    }
}
