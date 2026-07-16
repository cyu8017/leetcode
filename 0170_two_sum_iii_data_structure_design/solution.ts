// LeetCode 0170 - Two Sum III - Data structure design
// https://leetcode.com/problems/two-sum-iii-data-structure-design/

export class TwoSum {
    private readonly counts = new Map<number, number>();

    add(number: number): null {
        this.counts.set(number, (this.counts.get(number) ?? 0) + 1);
        return null;
    }

    find(value: number): boolean {
        for (const [number, count] of this.counts) {
            const complement = value - number;
            if (complement === number) {
                if (count >= 2) {
                    return true;
                }
            } else if (this.counts.has(complement)) {
                return true;
            }
        }
        return false;
    }
}