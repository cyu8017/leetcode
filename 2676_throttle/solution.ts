// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

export function throttle(fn: any, t: any): any {
    let last = -Infinity;
    let pending = null;
    let timer = null;
    const run = (...args) => {
        last = Date.now();
        fn(...args);
    };
    return function(...args) {
        const now = Date.now();
        const remaining = t - (now - last);
        if (remaining <= 0) {
            if (timer) { clearTimeout(timer); timer = null; }
            run(...args);
        } else {
            pending = args;
            if (!timer) {
                timer = setTimeout(() => {
                    timer = null;
                    if (pending) {
                        const a = pending;
                        pending = null;
                        run(...a);
                    }
                }, remaining);
            }
        }
    };
}
