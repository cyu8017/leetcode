// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

/**
 * @param {number[]} servers
 * @param {number[]} tasks
 * @return {number[]}
 */
var assignTasks = function(servers, tasks) {
    const cmp = (a, b) => {
        for (let i = 0; i < a.length; i++) {
            if (a[i] !== b[i]) return a[i] - b[i];
        }
        return 0;
    };
    const push = (heap, item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (cmp(heap[p], heap[i]) <= 0) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = (heap) => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let t = i;
                const l = i * 2 + 1, r = l + 1;
                if (l < heap.length && cmp(heap[l], heap[t]) < 0) t = l;
                if (r < heap.length && cmp(heap[r], heap[t]) < 0) t = r;
                if (t === i) break;
                [heap[t], heap[i]] = [heap[i], heap[t]];
                i = t;
            }
        }
        return top;
    };

    const available = [];
    for (let i = 0; i < servers.length; i++) push(available, [servers[i], i]);
    const busy = [];
    const answer = [];
    let time = 0;

    for (let moment = 0; moment < tasks.length; moment++) {
        const task = tasks[moment];
        time = Math.max(time, moment);
        while (busy.length && busy[0][0] <= time) {
            const [, weight, index] = pop(busy);
            push(available, [weight, index]);
        }
        while (!available.length) {
            time = busy[0][0];
            while (busy.length && busy[0][0] <= time) {
                const [, weight, index] = pop(busy);
                push(available, [weight, index]);
            }
        }
        const [weight, index] = pop(available);
        push(busy, [time + task, weight, index]);
        answer.push(index);
    }
    return answer;
};
