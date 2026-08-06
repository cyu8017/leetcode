<?php
class TreeAncestor {
    private $up;

    function __construct($n, $parent) {
        $width = max(1, intval(log($n, 2)) + 1);
        $this->up = [$parent];
        for ($bit = 1; $bit < $width; $bit++) {
            $prev = $this->up[$bit - 1];
            $row = [];
            foreach ($prev as $p) $row[] = $p === -1 ? -1 : $prev[$p];
            $this->up[] = $row;
        }
    }

    function getKthAncestor($node, $k) {
        $bit = 0;
        while ($k && $node !== -1) {
            if ($k & 1) {
                if ($bit >= count($this->up)) return -1;
                $node = $this->up[$bit][$node];
            }
            $bit++;
            $k >>= 1;
        }
        return $node;
    }
}
