export function isReflected(points: number[][]): boolean {
    const pointSet = new Set(points.map(([x, y]) => `${x},${y}`));
    const xs = points.map(([x]) => x);
    const minX = Math.min(...xs);
    const maxX = Math.max(...xs);
    const target = minX + maxX;

    for (const [x, y] of points) {
        if (!pointSet.has(`${target - x},${y}`)) return false;
    }

    return true;
}
