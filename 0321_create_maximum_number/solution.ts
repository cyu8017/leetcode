export function maxNumber(nums1: number[], nums2: number[], k: number): number[] {
    function pickMax(values: number[], count: number): number[] {
        let drop = values.length - count;
        const stack: number[] = [];
        for (const value of values) {
            while (drop > 0 && stack.length > 0 && stack[stack.length - 1] < value) {
                stack.pop();
                drop -= 1;
            }
            stack.push(value);
        }
        return stack.slice(0, count);
    }
    function compareSuffix(first: number[], left: number, second: number[], right: number): number {
        while (left < first.length && right < second.length) {
            if (first[left] !== second[right]) return first[left] - second[right];
            left += 1;
            right += 1;
        }
        return (first.length - left) - (second.length - right);
    }
    function merge(first: number[], second: number[]): number[] {
        const result: number[] = [];
        let left = 0;
        let right = 0;
        while (left < first.length && right < second.length) {
            if (compareSuffix(first, left, second, right) > 0) result.push(first[left++]);
            else result.push(second[right++]);
        }
        return result.concat(first.slice(left)).concat(second.slice(right));
    }
    function compareLists(a: number[], b: number[]): number {
        for (let index = 0; index < Math.max(a.length, b.length); index += 1) {
            const av = a[index] ?? -1;
            const bv = b[index] ?? -1;
            if (av !== bv) return av - bv;
        }
        return 0;
    }
    let best: number[] = [];
    for (let takeFirst = Math.max(0, k - nums2.length); takeFirst <= Math.min(k, nums1.length); takeFirst += 1) {
        const candidate = merge(pickMax(nums1, takeFirst), pickMax(nums2, k - takeFirst));
        if (compareLists(candidate, best) > 0) best = candidate;
    }
    return best;
}
