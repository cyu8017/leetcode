<?php
// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker {
    private $freq = [];
    private $count = [];

    function add($number) {
        $old = $this->freq[$number] ?? 0;
        if ($old > 0) $this->count[$old] = ($this->count[$old] ?? 0) - 1;
        $this->freq[$number] = $old + 1;
        $this->count[$old + 1] = ($this->count[$old + 1] ?? 0) + 1;
    }

    function deleteOne($number) {
        $old = $this->freq[$number] ?? 0;
        if ($old === 0) return;
        $this->count[$old] = ($this->count[$old] ?? 0) - 1;
        $this->freq[$number] = $old - 1;
        if ($old - 1 > 0) $this->count[$old - 1] = ($this->count[$old - 1] ?? 0) + 1;
    }

    function hasFrequency($frequency) {
        return ($this->count[$frequency] ?? 0) > 0;
    }
}
