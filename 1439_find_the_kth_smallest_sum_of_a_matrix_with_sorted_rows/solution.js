var kthSmallest = function(mat, k) {
    let sums = [0];
    for (const row of mat) {
        const next = []; for (const sum of sums) for (const value of row) next.push(sum + value);
        next.sort((a, b) => a - b); sums = next.slice(0, k);
    } return sums[k - 1];
};
