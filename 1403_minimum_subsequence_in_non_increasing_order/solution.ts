// LeetCode 1403: Minimum Subsequence In Non Increasing Order

function minSubsequence(nums: any): any {
    nums.sort((a, b: any): any => b - a);
    const total = nums.reduce((sum, value: any): any => sum + value, 0), result = [];
    let selected = 0;
    for (const value of nums) { selected += value; result.push(value); if (selected > total - selected) break; }
    return result;
}
