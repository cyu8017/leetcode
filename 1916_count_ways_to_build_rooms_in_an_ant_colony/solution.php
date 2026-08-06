<?php
// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

class Solution {
    private $mod = 1000000007;
    private $children;
    private $fact;
    private $invFact;

    /**
     * @param Integer[] $prevRoom
     * @return Integer
     */
    function waysToBuildRooms($prevRoom) {
        $n = count($prevRoom);
        $this->children = array_fill(0, $n, []);
        for ($room = 0; $room < $n; $room++) {
            $prev = $prevRoom[$room];
            if ($prev !== -1) {
                $this->children[$prev][] = $room;
            }
        }

        $this->fact = array_fill(0, $n + 1, 1);
        $this->invFact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) {
            $this->fact[$i] = ($this->fact[$i - 1] * $i) % $this->mod;
        }
        $this->invFact[$n] = $this->modPow($this->fact[$n], $this->mod - 2, $this->mod);
        for ($i = $n; $i > 0; $i--) {
            $this->invFact[$i - 1] = ($this->invFact[$i] * $i) % $this->mod;
        }

        return $this->dfs(0)[1];
    }

    private function comb($a, $b) {
        return $this->fact[$a]
            * $this->invFact[$b] % $this->mod
            * $this->invFact[$a - $b] % $this->mod;
    }

    private function dfs($node) {
        $size = 0;
        $ways = 1;
        foreach ($this->children[$node] as $child) {
            [$childSize, $childWays] = $this->dfs($child);
            $ways = $ways * $childWays % $this->mod * $this->comb($size + $childSize, $childSize) % $this->mod;
            $size += $childSize;
        }
        return [$size + 1, $ways];
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
