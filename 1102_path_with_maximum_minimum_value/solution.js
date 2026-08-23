// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumMinimumPath = function(grid) {
    const m = grid.length, n = grid[0].length;
    const heap = [[-grid[0][0], 0, 0]];
    const seen = new Set(["0,0"]);
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let smallest = i;
                const l = 2 * i + 1, r = 2 * i + 2;
                if (l < heap.length && heap[l][0] < heap[smallest][0]) smallest = l;
                if (r < heap.length && heap[r][0] < heap[smallest][0]) smallest = r;
                if (smallest === i) break;
                [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return top;
    };
    while (heap.length) {
        const [val, r, c] = pop();
        if (r === m - 1 && c === n - 1) return -val;
        for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
            const nr = r + dr, nc = c + dc;
            const key = `${nr},${nc}`;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen.has(key)) {
                seen.add(key);
                push([Math.max(val, -grid[nr][nc]), nr, nc]);
            }
        }
    }
    return grid[0][0];
};
