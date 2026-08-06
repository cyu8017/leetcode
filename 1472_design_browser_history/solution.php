<?php
class BrowserHistory {
    private $history;
    private $index;

    function __construct($homepage) {
        $this->history = [$homepage];
        $this->index = 0;
    }

    function visit($url) {
        $this->history = array_slice($this->history, 0, $this->index + 1);
        $this->history[] = $url;
        $this->index++;
    }

    function back($steps) {
        $this->index = max(0, $this->index - $steps);
        return $this->history[$this->index];
    }

    function forward($steps) {
        $this->index = min(count($this->history) - 1, $this->index + $steps);
        return $this->history[$this->index];
    }
}
