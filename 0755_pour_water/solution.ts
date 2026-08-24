// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

export function pourWater(heights: number[], volume: number, k: number): number[] {
    for (let v = 0; v < volume; v++) {
        let index = k;
        for (let i = k - 1; i >= 0; i--) {
            if (heights[i] > heights[index]) break;
            if (heights[i] < heights[index]) index = i;
        }
        if (index !== k) { heights[index]++; continue; }
        index = k;
        for (let i = k + 1; i < heights.length; i++) {
            if (heights[i] > heights[index]) break;
            if (heights[i] < heights[index]) index = i;
        }
        heights[index]++;
    }
    return heights;
}
