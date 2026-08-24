// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

export function totalWaviness(num1: any, num2: any): any {
    const F = (x) => {
        const nums = [];
        while (x > 0) {
            nums.push(x % 10);
            x = Math.floor(x / 10);
        }
        const m = nums.length;
        if (m < 3) return 0;
        let s = 0;
        for (let i = 1; i < m - 1; i++) {
            if ((nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
                (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])) s++;
        }
        return s;
    };
    let ans = 0;
    for (let x = num1; x <= num2; x++) ans += F(x);
    return ans;
}
