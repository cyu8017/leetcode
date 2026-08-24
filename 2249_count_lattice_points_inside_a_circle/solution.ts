// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

export function countLatticePoints(circles: number[][]): number {
    const seen = new Set();
    for (const c of circles) {
        const x = c[0], y = c[1], r = c[2];
        for (let i = x - r; i <= x + r; i++)
            for (let j = y - r; j <= y + r; j++)
                if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r)
                    seen.add(i + ',' + j);
    }
    return seen.size;
}
