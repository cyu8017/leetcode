// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

export function maxArea(height: number[]): number {
    let left = 0;
    let right = height.length - 1;
    let best = 0;

    while (left < right) {
        const width = right - left;
        best = Math.max(best, Math.min(height[left], height[right]) * width);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return best;
}
