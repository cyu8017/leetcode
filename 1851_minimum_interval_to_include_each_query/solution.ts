// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

function minInterval(intervals: number[][], queries: number[]): number[] {
    intervals = intervals.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    const indexed = queries.map((q, i) => [q, i]).sort((a, b) => a[0] - b[0]);
    const heap: number[][] = [];
    const answer = new Array(queries.length).fill(-1);
    let idx = 0;

    const push = (size: number, right: number) => {
        heap.push([size, right]);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] < heap[i][0] || (heap[p][0] === heap[i][0] && heap[p][1] <= heap[i][1])) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = (): number[] => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last!;
            let i = 0;
            while (true) {
                let t = i;
                const l = i * 2 + 1, r = l + 1;
                if (l < heap.length && (heap[l][0] < heap[t][0] || (heap[l][0] === heap[t][0] && heap[l][1] < heap[t][1]))) t = l;
                if (r < heap.length && (heap[r][0] < heap[t][0] || (heap[r][0] === heap[t][0] && heap[r][1] < heap[t][1]))) t = r;
                if (t === i) break;
                [heap[t], heap[i]] = [heap[i], heap[t]];
                i = t;
            }
        }
        return top;
    };

    for (const [query, queryIdx] of indexed) {
        while (idx < intervals.length && intervals[idx][0] <= query) {
            const [left, right] = intervals[idx++];
            push(right - left + 1, right);
        }
        while (heap.length && heap[0][1] < query) pop();
        if (heap.length) answer[queryIdx] = heap[0][0];
    }
    return answer;
}
