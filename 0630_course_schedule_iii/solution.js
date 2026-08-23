// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

/**
 * @param {number[][]} courses
 * @return {number}
 */
var scheduleCourse = function(courses) {
    courses.sort((a, b) => a[1] - b[1]);
    const heap = [];
    const push = (v) => {
        heap.push(v);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] >= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let largest = i;
                const l = i * 2 + 1, r = i * 2 + 2;
                if (l < heap.length && heap[l] > heap[largest]) largest = l;
                if (r < heap.length && heap[r] > heap[largest]) largest = r;
                if (largest === i) break;
                [heap[i], heap[largest]] = [heap[largest], heap[i]];
                i = largest;
            }
        }
        return top;
    };
    let time = 0;
    for (const [duration, lastDay] of courses) {
        if (time + duration <= lastDay) {
            push(duration);
            time += duration;
        } else if (heap.length && heap[0] > duration) {
            time += duration - pop();
            push(duration);
        }
    }
    return heap.length;
};
