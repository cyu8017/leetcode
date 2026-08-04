var BrowserHistory = function(homepage) {
    this.history = [homepage];
    this.index = 0;
};

BrowserHistory.prototype.visit = function(url) {
    this.history.length = this.index + 1;
    this.history.push(url);
    this.index++;
};

BrowserHistory.prototype.back = function(steps) {
    this.index = Math.max(0, this.index - steps);
    return this.history[this.index];
};

BrowserHistory.prototype.forward = function(steps) {
    this.index = Math.min(this.history.length - 1, this.index + steps);
    return this.history[this.index];
};
