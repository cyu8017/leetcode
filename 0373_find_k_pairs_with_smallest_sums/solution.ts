export function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    if (!nums1.length || !nums2.length || k === 0) return [];

    const heap: Array<[number, number, number]> = [];
    const push = (value: number, index1: number, index2: number) => {
        let position = heap.length;
        heap.push([value, index1, index2]);
        while (position > 0) {
            const parent = Math.floor((position - 1) / 2);
            if (heap[parent][0] <= heap[position][0]) break;
            [heap[parent], heap[position]] = [heap[position], heap[parent]];
            position = parent;
        }
    };
    const pop = (): [number, number, number] => {
        const top = heap[0];
        const last = heap.pop()!;
        if (!heap.length) return top;
        heap[0] = last;
        let position = 0;
        while (true) {
            let smallest = position;
            const left = position * 2 + 1;
            const right = position * 2 + 2;
            if (left < heap.length && heap[left][0] < heap[smallest][0]) smallest = left;
            if (right < heap.length && heap[right][0] < heap[smallest][0]) smallest = right;
            if (smallest === position) break;
            [heap[smallest], heap[position]] = [heap[position], heap[smallest]];
            position = smallest;
        }
        return top;
    };

    for (let index = 0; index < Math.min(nums1.length, k); index += 1) {
        push(nums1[index] + nums2[0], index, 0);
    }

    const result: number[][] = [];
    while (heap.length && result.length < k) {
        const [, index1, index2] = pop();
        result.push([nums1[index1], nums2[index2]]);
        if (index2 + 1 < nums2.length) push(nums1[index1] + nums2[index2 + 1], index1, index2 + 1);
    }

    return result;
}
