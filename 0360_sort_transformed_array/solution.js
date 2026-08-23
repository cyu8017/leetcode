// LeetCode 0360 - Sort Transformed Array
var sortTransformedArray = function(nums, a, b, c) {
    const transform = (value) => a * value * value + b * value + c;
    let left = 0;
    let right = nums.length - 1;
    const result = new Array(nums.length);
    let index = a > 0 ? nums.length - 1 : 0;
    const step = a > 0 ? -1 : 1;

    while (left <= right) {
        const leftValue = transform(nums[left]);
        const rightValue = transform(nums[right]);

        if (a > 0) {
            if (leftValue > rightValue) {
                result[index] = leftValue;
                left += 1;
            } else {
                result[index] = rightValue;
                right -= 1;
            }
        } else if (leftValue < rightValue) {
            result[index] = leftValue;
            left += 1;
        } else {
            result[index] = rightValue;
            right -= 1;
        }

        index += step;
    }

    return result;
};
