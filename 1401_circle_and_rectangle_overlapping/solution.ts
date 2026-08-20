// LeetCode 1401: Circle And Rectangle Overlapping

function checkOverlap(radius: any, xCenter: any, yCenter: any, x1: any, y1: any, x2: any, y2: any): any {
    const x = Math.max(x1, Math.min(xCenter, x2)), y = Math.max(y1, Math.min(yCenter, y2));
    return (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2;
}
