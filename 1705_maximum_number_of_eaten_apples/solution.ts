// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

function eatenApples(apples: number[], days: number[]): number {
    const heap: [number, number][] = [];

    const push = (item: [number, number]): void => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = (i - 1) >> 1;
            if (heap[parent][0] <= heap[i][0]) {
                break;
            }
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };

    const pop = (): [number, number] => {
        const top = heap[0];
        const last = heap.pop()!;
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let smallest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                if (left < heap.length && heap[left][0] < heap[smallest][0]) {
                    smallest = left;
                }
                if (right < heap.length && heap[right][0] < heap[smallest][0]) {
                    smallest = right;
                }
                if (smallest === i) {
                    break;
                }
                [heap[smallest], heap[i]] = [heap[i], heap[smallest]];
                i = smallest;
            }
        }
        return top;
    };

    const n = apples.length;
    let day = 0;
    let eaten = 0;
    while (day < n || heap.length > 0) {
        if (day < n && apples[day] > 0) {
            push([day + days[day], apples[day]]);
        }
        while (heap.length > 0 && heap[0][0] <= day) {
            pop();
        }
        if (heap.length > 0) {
            const [expire, count] = pop();
            eaten++;
            if (count > 1) {
                push([expire, count - 1]);
            }
        }
        day++;
    }
    return eaten;
}
