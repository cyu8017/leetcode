// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

export function stableMountains(height: any, threshold: any): any {
    const ans = [];
    for (let i = 1; i < height.length; i++) {
        if (height[i - 1] > threshold) ans.push(i);
    }
    return ans;
}
