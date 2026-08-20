function getStrongest(arr: any, k: any): any {
    arr.sort((a, b: any): any => a - b);
    const median = arr[Math.floor((arr.length - 1) / 2)];
    arr.sort((a, b: any): any => Math.abs(b - median) - Math.abs(a - median) || b - a);
    return arr.slice(0, k);
}
