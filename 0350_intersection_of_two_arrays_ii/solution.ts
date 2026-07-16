export function intersect(nums1: number[], nums2: number[]): number[] {
    const counts = new Map<number, number>();
    for (const num of nums1) {
        counts.set(num, (counts.get(num) ?? 0) + 1);
    }

    const result: number[] = [];
    for (const num of nums2) {
        if ((counts.get(num) ?? 0) > 0) {
            result.push(num);
            counts.set(num, counts.get(num)! - 1);
        }
    }

    return result;
}
