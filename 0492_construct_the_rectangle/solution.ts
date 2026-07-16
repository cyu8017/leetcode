// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

export class Solution {
    constructRectangle(area: number): number[] {
        const limit = Math.floor(Math.sqrt(area));
        for (let width = limit; width >= 1; width -= 1) {
            if (area % width === 0) return [area / width, width];
        }
        return [area, 1];
    }
}
