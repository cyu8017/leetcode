<?php
class FirstUnique {
    private $counts = [];
    private $unique = [];

    function __construct($nums) {
        foreach ($nums as $value) $this->add($value);
    }

    function showFirstUnique() {
        foreach ($this->unique as $value => $_) return $value;
        return -1;
    }

    function add($value) {
        $this->counts[$value] = ($this->counts[$value] ?? 0) + 1;
        if ($this->counts[$value] === 1) $this->unique[$value] = true;
        else unset($this->unique[$value]);
    }
}
