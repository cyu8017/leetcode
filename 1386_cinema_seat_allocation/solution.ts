// LeetCode 1386: Cinema Seat Allocation

function maxNumberOfFamilies(n: any, reservedSeats: any): any {
    const reserved = new Map();
    for (const [row, seat] of reservedSeats) reserved.set(row, (reserved.get(row) || 0) | (1 << seat));
    let families = 2 * (n - reserved.size);
    for (const mask of reserved.values()) {
        const left = 0b0000011110, middle = 0b0111100000, right = 0b1111000000;
        if ((mask & left) === 0 && (mask & right) === 0) families += 2;
        else if ((mask & left) === 0 || (mask & middle) === 0 || (mask & right) === 0) families++;
    }
    return families;
}
