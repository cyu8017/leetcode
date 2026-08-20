// LeetCode 1399: Count Largest Group

function countLargestGroup(n: any): any {
    const count = new Map();
    for (let value = 1; value <= n; value++) {
        let sum = 0, number = value;
        while (number) { sum += number % 10; number = Math.floor(number / 10); }
        count.set(sum, (count.get(sum) || 0) + 1);
    }
    const largest = Math.max(...count.values());
    return [...count.values()].filter((size: any): any => size === largest).length;
}
