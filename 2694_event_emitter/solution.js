// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

var EventEmitter = function() {
    this.handlers = new Map();
};

EventEmitter.prototype.subscribe = function(eventName, callback) {
    if (!this.handlers.has(eventName)) this.handlers.set(eventName, []);
    const list = this.handlers.get(eventName);
    list.push(callback);
    return {
        unsubscribe: () => {
            const idx = list.indexOf(callback);
            if (idx >= 0) list.splice(idx, 1);
        },
    };
};

EventEmitter.prototype.emit = function(eventName, args = []) {
    const list = this.handlers.get(eventName) || [];
    return list.map((cb) => cb(...args));
};
