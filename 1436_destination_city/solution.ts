function destCity(paths: any): any {
    const starts = new Set(paths.map((path: any): any => path[0])); return paths.find((path: any): any => !starts.has(path[1]))[1];
}
