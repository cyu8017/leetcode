// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

function minElements(nums: number[], limit: number, goal: number): number {
    let sum = 0;
    for (const num of nums) {
        sum += num;
    }
    const diff = Math.abs(sum - goal);
    let count = Math.floor(diff / limit);
    if (count * limit < diff) {
        count++;
    }
    return count;
}
