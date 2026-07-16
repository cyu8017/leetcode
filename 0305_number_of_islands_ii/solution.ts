// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

export function numIslands2(m: number, n: number, positions: number[][]): number[] {
    const parent = new Map<number, number>();
    const rank = new Map<number, number>();

    function find(index: number): number {
        if (!parent.has(index)) {
            parent.set(index, index);
            rank.set(index, 0);
        }
        if (parent.get(index) !== index) {
            parent.set(index, find(parent.get(index) as number));
        }
        return parent.get(index) as number;
    }

    function union(left: number, right: number): boolean {
        const rootLeft = find(left);
        const rootRight = find(right);
        if (rootLeft === rootRight) {
            return false;
        }
        if ((rank.get(rootLeft) as number) < (rank.get(rootRight) as number)) {
            parent.set(rootLeft, rootRight);
        } else {
            parent.set(rootRight, rootLeft);
            if (rank.get(rootLeft) === rank.get(rootRight)) {
                rank.set(rootLeft, (rank.get(rootLeft) as number) + 1);
            }
        }
        return true;
    }

    const directions: [number, number][] = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const result: number[] = [];
    let islands = 0;
    for (const [row, col] of positions) {
        const index = row * n + col;
        if (parent.has(index)) {
            result.push(islands);
            continue;
        }
        parent.set(index, index);
        islands += 1;
        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                const neighbor = nr * n + nc;
                if (parent.has(neighbor) && union(index, neighbor)) {
                    islands -= 1;
                }
            }
        }
        result.push(islands);
    }
    return result;
}
