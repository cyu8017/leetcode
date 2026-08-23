// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

var makeImmutable = function(obj) {
    const wrap = (val) => {
        if (val === null || typeof val !== "object") return val;
        if (Array.isArray(val)) {
            return new Proxy(val, {
                set(target, prop) {
                    throw `Error Modifying Index: ${String(prop)}`;
                },
                get(target, prop) {
                    if (["pop", "push", "shift", "unshift", "splice", "sort", "reverse"].includes(prop)) {
                        return () => { throw `Error Calling Method: ${prop}`; };
                    }
                    const v = target[prop];
                    return typeof v === "function" ? v.bind(target) : wrap(v);
                },
            });
        }
        return new Proxy(val, {
            set(target, prop) {
                throw `Error Modifying: ${String(prop)}`;
            },
            get(target, prop) {
                const v = target[prop];
                return typeof v === "function" ? v.bind(target) : wrap(v);
            },
        });
    };
    return wrap(obj);
};
