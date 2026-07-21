// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

function minWastedSpace(packages: number[], boxes: number[][]): number {
    packages = packages.slice().sort((a, b) => a - b);
    const prefix: number[] = [];
    let running = 0;
    for (const p of packages) {
        running += p;
        prefix.push(running);
    }
    let answer = Infinity;

    const bisectRight = (arr: number[], x: number, lo: number) => {
        let hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    for (const supplier of boxes) {
        const sorted = supplier.slice().sort((a, b) => a - b);
        let start = 0, wasted = 0;
        for (const box of sorted) {
            const end = bisectRight(packages, box, start);
            if (end === start) continue;
            const packageSum = prefix[end - 1] - (start ? prefix[start - 1] : 0);
            wasted += box * (end - start) - packageSum;
            start = end;
        }
        if (start === packages.length) answer = Math.min(answer, wasted);
    }
    return answer === Infinity ? -1 : answer % 1000000007;
}
