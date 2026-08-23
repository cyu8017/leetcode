// LeetCode 0327 - Count of Range Sum
var countRangeSum = function(nums, lower, upper) {
    const prefix = [0];
    for (const num of nums) prefix.push(prefix[prefix.length - 1] + num);
    const temp = Array(prefix.length).fill(0);
    function mergeSort(left, right) {
        if (left >= right) return 0;
        const mid = Math.floor((left + right) / 2);
        let count = mergeSort(left, mid) + mergeSort(mid + 1, right);
        let start = mid + 1;
        let end = mid + 1;
        for (let index = left; index <= mid; index += 1) {
            while (start <= right && prefix[start] - prefix[index] < lower) start += 1;
            while (end <= right && prefix[end] - prefix[index] <= upper) end += 1;
            count += end - start;
        }
        let tempLeft = left;
        let tempRight = mid + 1;
        let write = left;
        while (tempLeft <= mid && tempRight <= right) {
            if (prefix[tempLeft] <= prefix[tempRight]) temp[write++] = prefix[tempLeft++];
            else temp[write++] = prefix[tempRight++];
        }
        while (tempLeft <= mid) temp[write++] = prefix[tempLeft++];
        while (tempRight <= right) temp[write++] = prefix[tempRight++];
        for (let index = left; index <= right; index += 1) prefix[index] = temp[index];
        return count;
    }
    return mergeSort(0, prefix.length - 1);
};
