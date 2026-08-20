"use strict";
function avoidFlood(rains) {
    const answer = Array(rains.length).fill(-1), full = new Map(), dryDays = [], parent = [];
    const find = (index) => {
        if (index === parent.length)
            return index;
        if (parent[index] === index)
            return index;
        parent[index] = find(parent[index]);
        return parent[index];
    };
    const lowerBound = (value) => {
        let low = 0, high = dryDays.length;
        while (low < high) {
            const middle = Math.floor((low + high) / 2);
            if (dryDays[middle] <= value)
                low = middle + 1;
            else
                high = middle;
        }
        return low;
    };
    for (let day = 0; day < rains.length; day++) {
        const lake = rains[day];
        if (lake === 0) {
            answer[day] = 1;
            parent[dryDays.length] = dryDays.length;
            dryDays.push(day);
        }
        else {
            if (full.has(lake)) {
                const position = find(lowerBound(full.get(lake)));
                if (position === dryDays.length)
                    return [];
                answer[dryDays[position]] = lake;
                parent[position] = find(position + 1);
            }
            full.set(lake, day);
        }
    }
    return answer;
}
