"use strict";
class BrowserHistory {
    constructor(homepage) {
        this.history = [homepage];
        this.index = 0;
    }
    visit(url) {
        this.history.length = this.index + 1;
        this.history.push(url);
        this.index++;
    }
    back(steps) {
        this.index = Math.max(0, this.index - steps);
        return this.history[this.index];
    }
    forward(steps) {
        this.index = Math.min(this.history.length - 1, this.index + steps);
        return this.history[this.index];
    }
}
