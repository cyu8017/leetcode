function minDays(bloomDay: any, m: any, k: any): any {
    if (m * k > bloomDay.length) return -1;
    const canMake = (day: any): any => {
        let bouquets = 0, flowers = 0;
        for (const bloom of bloomDay) {
            flowers = bloom <= day ? flowers + 1 : 0;
            if (flowers === k) {
                bouquets++;
                flowers = 0;
            }
        }
        return bouquets >= m;
    };
    let low = Math.min(...bloomDay), high = Math.max(...bloomDay);
    while (low < high) {
        const middle = Math.floor((low + high) / 2);
        if (canMake(middle)) high = middle;
        else low = middle + 1;
    }
    return low;
}
