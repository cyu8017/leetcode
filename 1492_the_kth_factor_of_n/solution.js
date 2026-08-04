var kthFactor = function(n, k) {
    for (let factor = 1; factor <= n; factor++) {
        if (n % factor === 0 && --k === 0) return factor;
    }
    return -1;
};
