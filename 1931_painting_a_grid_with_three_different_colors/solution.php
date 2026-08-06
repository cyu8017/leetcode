<?php
class Solution {
    private $m;
    private $n;
    private $states = [];
    private $compat = [];
    private $memo = [];
    private const MOD = 1000000007;

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function colorTheGrid($m, $n) {
        $this->m = $m;
        $this->n = $n;
        $this->states = [];
        $this->compat = [];
        $this->memo = [];

        $total = (int)pow(3, $m);
        for ($s = 0; $s < $total; $s++) {
            if ($this->validColumn($s)) {
                $this->states[] = $s;
            }
        }
        foreach ($this->states as $a) {
            $list = [];
            $ca = $this->colors($a);
            foreach ($this->states as $b) {
                $cb = $this->colors($b);
                $ok = true;
                for ($i = 0; $i < $m; $i++) {
                    if ($ca[$i] === $cb[$i]) {
                        $ok = false;
                        break;
                    }
                }
                if ($ok) {
                    $list[] = $b;
                }
            }
            $this->compat[$a] = $list;
        }
        return $this->dp(0, -1);
    }

    private function dp($col, $prev) {
        if ($col === $this->n) {
            return 1;
        }
        $key = ($col << 20) | ($prev + 1);
        if (isset($this->memo[$key])) {
            return $this->memo[$key];
        }
        $total = 0;
        $cands = $prev === -1 ? $this->states : $this->compat[$prev];
        foreach ($cands as $cur) {
            $total = ($total + $this->dp($col + 1, $cur)) % self::MOD;
        }
        $this->memo[$key] = $total;
        return $total;
    }

    private function validColumn($mask) {
        $prev = -1;
        for ($i = 0; $i < $this->m; $i++) {
            $c = $mask % 3;
            if ($c === $prev) {
                return false;
            }
            $prev = $c;
            $mask = intdiv($mask, 3);
        }
        return true;
    }

    private function colors($mask) {
        $cols = [];
        for ($i = 0; $i < $this->m; $i++) {
            $cols[] = $mask % 3;
            $mask = intdiv($mask, 3);
        }
        return $cols;
    }
}
