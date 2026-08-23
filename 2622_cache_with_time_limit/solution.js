// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

var TimeLimitedCache = function() {
    this.data = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const e = this.data.get(key);
    const alive = e !== undefined && e.expire > now;
    this.data.set(key, { value: value, expire: now + duration });
    return alive;
};

TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();
    const e = this.data.get(key);
    if (e === undefined || e.expire <= now) return -1;
    return e.value;
};

TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let cnt = 0;
    for (const [k, e] of this.data) {
        if (e.expire > now) cnt++;
        else this.data.delete(k);
    }
    return cnt;
};
