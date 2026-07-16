// LeetCode 0391 - Perfect Rectangle
export function isRectangleCover(rectangles: number[][]): boolean {
    const points = new Set<string>();
    let area = 0;
    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;

    for (const [x1, y1, x2, y2] of rectangles) {
        area += (x2 - x1) * (y2 - y1);
        minX = Math.min(minX, x1);
        minY = Math.min(minY, y1);
        maxX = Math.max(maxX, x2);
        maxY = Math.max(maxY, y2);

        for (const point of [`${x1},${y1}`, `${x1},${y2}`, `${x2},${y1}`, `${x2},${y2}`]) {
            if (points.has(point)) points.delete(point);
            else points.add(point);
        }
    }

    const corners = new Set([`${minX},${minY}`, `${minX},${maxY}`, `${maxX},${minY}`, `${maxX},${maxY}`]);
    if (points.size !== 4 || [...corners].some((point) => !points.has(point))) return false;
    return area === (maxX - minX) * (maxY - minY);
}
