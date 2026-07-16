export function topKFrequent(nums: number[], k: number): number[] {
    const counts = new Map<number, number>();
    for (const num of nums) {
        counts.set(num, (counts.get(num) ?? 0) + 1);
    }

    const buckets = Array.from({ length: nums.length + 1 }, () => [] as number[]);
    for (const [value, count] of counts.entries()) {
        buckets[count].push(value);
    }

    const result: number[] = [];
    for (let index = buckets.length - 1; index >= 0; index -= 1) {
        for (const value of buckets[index]) {
            result.push(value);
            if (result.length === k) return result;
        }
    }

    return result;
}
