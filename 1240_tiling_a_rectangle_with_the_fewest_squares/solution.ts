// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

function tilingRectangle(n: number, m: number): number {
    if (n > m) [n, m] = [m, n];
    const heights = Array(m).fill(0);
    let best = n * m;
    function search(used) {
        if (used >= best) return;
        const low = Math.min(...heights);
        if (low === n) {
            best = used;
            return;
        }
        const left = heights.indexOf(low);
        let right = left;
        while (right < m && heights[right] === low) right++;
        const maxSize = Math.min(n - low, right - left);
        for (let size = maxSize; size >= 1; size--) {
            for (let i = left; i < left + size; i++) heights[i] = low + size;
            search(used + 1);
            for (let i = left; i < left + size; i++) heights[i] = low;
        }
    }
    search(0);
    return best;
}
