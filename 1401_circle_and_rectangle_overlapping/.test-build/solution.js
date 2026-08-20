"use strict";
// LeetCode 1401: Circle And Rectangle Overlapping
function checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2) {
    const x = Math.max(x1, Math.min(xCenter, x2)), y = Math.max(y1, Math.min(yCenter, y2));
    return (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2;
}
