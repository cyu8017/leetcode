// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

var ImmutableHelper = function(obj) {
    this.obj = obj;
};

ImmutableHelper.prototype.produce = function(mutator) {
    const clones = new Map();
    const isObj = (v) => v !== null && typeof v === "object";

    const getClone = (original) => {
        if (clones.has(original)) return clones.get(original);
        const copy = Array.isArray(original) ? original.slice() : Object.assign({}, original);
        clones.set(original, copy);
        return copy;
    };

    const proxyFor = (node, onReplace) => new Proxy(node, {
        get(t, prop) {
            const val = t[prop];
            if (isObj(val)) {
                return proxyFor(val, (childClone) => {
                    const clone = getClone(t);
                    clone[prop] = childClone;
                    onReplace(clone);
                });
            }
            return typeof val === "function" ? val.bind(t) : val;
        },
        set(t, prop, value) {
            const clone = getClone(t);
            clone[prop] = value;
            onReplace(clone);
            return true;
        },
        deleteProperty(t, prop) {
            const clone = getClone(t);
            delete clone[prop];
            onReplace(clone);
            return true;
        },
    });

    let rootResult = this.obj;
    mutator(proxyFor(this.obj, (clone) => { rootResult = clone; }));
    return rootResult;
};
