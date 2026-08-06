<?php
class Solution {
    private $mod = 1000000007;
    private $n;
    private $s1;
    private $s2;
    private $evil;
    private $m;
    private $trans;
    private $memo;

    function findGoodStrings($n, $s1, $s2, $evil) {
        $this->n = $n;
        $this->s1 = $s1;
        $this->s2 = $s2;
        $this->evil = $evil;
        $this->m = strlen($evil);
        $pi = array_fill(0, $this->m, 0);
        for ($i = 1; $i < $this->m; $i++) {
            $j = $pi[$i - 1];
            while ($j && $evil[$i] !== $evil[$j]) $j = $pi[$j - 1];
            if ($evil[$i] === $evil[$j]) $j++;
            $pi[$i] = $j;
        }
        $this->trans = array_fill(0, $this->m, array_fill(0, 26, 0));
        for ($j = 0; $j < $this->m; $j++) {
            for ($x = 0; $x < 26; $x++) {
                $c = chr(97 + $x);
                $k = $j;
                while ($k && $evil[$k] !== $c) $k = $pi[$k - 1];
                if ($evil[$k] === $c) $k++;
                $this->trans[$j][$x] = $k;
            }
        }
        $this->memo = [];
        return $this->dp(0, 0, 1, 1);
    }

    private function dp($i, $j, $lo, $hi) {
        if ($j === $this->m) return 0;
        if ($i === $this->n) return 1;
        $key = "$i,$j,$lo,$hi";
        if (isset($this->memo[$key])) return $this->memo[$key];
        $a = $lo ? ord($this->s1[$i]) - 97 : 0;
        $b = $hi ? ord($this->s2[$i]) - 97 : 25;
        $ans = 0;
        for ($x = $a; $x <= $b; $x++) {
            $ans = ($ans + $this->dp($i + 1, $this->trans[$j][$x], $lo && $x === $a ? 1 : 0, $hi && $x === $b ? 1 : 0)) % $this->mod;
        }
        return $this->memo[$key] = $ans;
    }
}
