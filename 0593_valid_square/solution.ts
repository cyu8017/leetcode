// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

export function validSquare(p1: number[], p2: number[], p3: number[], p4: number[]): boolean {
    const distSq = (a, b) => {
        const dx = a[0] - b[0], dy = a[1] - b[1];
        return dx * dx + dy * dy;
    };
    const points = [p1, p2, p3, p4];
    const distances = [];
    for (let i = 0; i < 4; ++i) {
        for (let j = i + 1; j < 4; ++j) distances.push(distSq(points[i], points[j]));
    }
    distances.sort((a, b) => a - b);
    return distances[0] > 0 && distances[0] === distances[1] && distances[1] === distances[2]
        && distances[2] === distances[3] && distances[4] === distances[5]
        && distances[4] === 2 * distances[0];
}
