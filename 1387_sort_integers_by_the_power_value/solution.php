<?php
class Solution {
    private $memo = [];
    function getKth($lo, $hi, $k) {
        $this->memo = [];
        $vals = range($lo, $hi);
        $self = $this;
        usort($vals, function($a, $b) use ($self) {
            $pa = $self->power($a);
            $pb = $self->power($b);
            if ($pa !== $pb) return $pa <=> $pb;
            return $a <=> $b;
        });
        return $vals[$k - 1];
    }
    function power($x) {
        if ($x === 1) return 0;
        if (isset($this->memo[$x])) return $this->memo[$x];
        return $this->memo[$x] = 1 + $this->power($x % 2 === 0 ? intdiv($x, 2) : 3 * $x + 1);
    }
}
