// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

export function minElement(nums: any): any {
    let ans = 1000000000;
    for (let num of nums) {
        let x = num, s = 0;
        while (x > 0) { s += x % 10; x = Math.floor(x / 10); }
        if (s < ans) ans = s;
    }
    return ans;
}
