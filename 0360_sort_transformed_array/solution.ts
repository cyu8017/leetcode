export function sortTransformedArray(nums: number[], a: number, b: number, c: number): number[] {
    const transform = (value: number): number => a * value * value + b * value + c;
    let left = 0;
    let right = nums.length - 1;
    const result = new Array<number>(nums.length);
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
}
