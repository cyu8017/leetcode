<?php
class SubrectangleQueries {
    private $rectangle;

    function __construct($rectangle) {
        $this->rectangle = $rectangle;
    }

    function updateSubrectangle($row1, $col1, $row2, $col2, $newValue) {
        for ($r = $row1; $r <= $row2; $r++) {
            for ($c = $col1; $c <= $col2; $c++) {
                $this->rectangle[$r][$c] = $newValue;
            }
        }
    }

    function getValue($row, $col) {
        return $this->rectangle[$row][$col];
    }
}
