<?php
// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

class Vector2D {
    private array $vec;
    private int $row = 0;
    private int $col = 0;

    function __construct(array $vec) {
        $this->vec = $vec;
        $this->advance();
    }

    function next(): int {
        $value = $this->vec[$this->row][$this->col];
        $this->col += 1;
        $this->advance();
        return $value;
    }

    function hasNext(): bool {
        $this->advance();
        return $this->row < count($this->vec);
    }

    private function advance(): void {
        while ($this->row < count($this->vec) && $this->col >= count($this->vec[$this->row])) {
            $this->row += 1;
            $this->col = 0;
        }
    }
}
