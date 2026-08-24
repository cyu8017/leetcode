<?php
// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

class ExamRoom {
    public $n;
    public $seats;

    /**
     * @param Integer $n
     */
    function __construct($n) {
        $this->n = $n;
        $this->seats = [];
    }

    /**
     * @return Integer
     */
    function seat() {
        if (!count($this->seats)) {
            $this->seats[] = 0;
            return 0;
        }
        $bestSeat = 0;
        $bestDist = $this->seats[0];
        $prev = $this->seats[0];
        foreach ($this->seats as $cur) {
            if ($cur === $prev) continue;
            $dist = intdiv($cur - $prev, 2);
            if ($dist > $bestDist) {
                $bestDist = $dist;
                $bestSeat = $prev + $dist;
            }
            $prev = $cur;
        }
        if ($this->n - 1 - $this->seats[count($this->seats) - 1] > $bestDist) $bestSeat = $this->n - 1;
        $this->seats[] = $bestSeat;
        sort($this->seats);
        return $bestSeat;
    }

    /**
     * @param Integer $p
     * @return NULL
     */
    function leave($p) {
        $idx = array_search($p, $this->seats, true);
        if ($idx !== false) array_splice($this->seats, $idx, 1);
    }
}
