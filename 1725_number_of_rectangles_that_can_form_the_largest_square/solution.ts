// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

function countGoodRectangles(rectangles: number[][]): number {
    let best = 0;
    let count = 0;
    for (const [a, b] of rectangles) {
        const side = Math.min(a, b);
        if (side > best) {
            best = side;
            count = 1;
        } else if (side === best) {
            count++;
        }
    }
    return count;
}
