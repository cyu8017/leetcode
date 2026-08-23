// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

/**
 * @param {Function} fn
 * @param {number} delay
 * @param {number} period
 * @return {number}
 */
var customInterval = function(fn, delay, period) {
    let count = 0;
    let cancelled = false;
    const id = customInterval._nextId = (customInterval._nextId || 1) + 1;
    if (!customInterval._timers) customInterval._timers = new Map();
    const schedule = () => {
        const t = setTimeout(() => {
            if (cancelled) return;
            fn();
            count++;
            schedule();
        }, delay + period * count);
        customInterval._timers.set(id, t);
    };
    schedule();
    customInterval._cancelled = customInterval._cancelled || new Map();
    customInterval._cancelled.set(id, () => {
        cancelled = true;
        const t = customInterval._timers.get(id);
        if (t) clearTimeout(t);
    });
    return id;
};

/**
 * @param {number} id
 * @return {void}
 */
var customClearInterval = function(id) {
    const cancel = customInterval._cancelled && customInterval._cancelled.get(id);
    if (cancel) cancel();
};
