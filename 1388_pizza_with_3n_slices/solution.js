// LeetCode 1388: Pizza With 3N Slices

var maxSizeSlices = function(slices) {
    const solve = array => {
        const picks = Math.floor(slices.length / 3);
        let previous = Array(picks + 1).fill(0), current = Array(picks + 1).fill(0);
        for (let i = 1; i <= array.length; i++) {
            const next = Array(picks + 1).fill(0);
            for (let j = 1; j <= Math.min(picks, Math.ceil(i / 2)); j++) next[j] = Math.max(current[j], previous[j - 1] + array[i - 1]);
            previous = current; current = next;
        }
        return current[picks];
    };
    return Math.max(solve(slices.slice(1)), solve(slices.slice(0, -1)));
};
