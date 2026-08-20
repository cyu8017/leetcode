// LeetCode 1413: Minimum Value To Get Positive Step By Step Sum

function minStartValue(nums: any): any {
    let sum = 0, minimum = 0;
    for (const value of nums) { sum += value; minimum = Math.min(minimum, sum); }
    return 1 - minimum;
}
