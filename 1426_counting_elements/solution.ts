function countElements(arr: any): any {
    const values = new Set(arr); return arr.reduce((count, x: any): any => count + values.has(x + 1), 0);
}
