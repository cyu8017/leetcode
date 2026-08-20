function maxDiff(num: any): any {
    const s = String(num);
    const maximum = Number(s.replace(new RegExp((s.match(/[0-8]/) || [""])[0], "g"), "9"));
    let target = s[0] === "1" ? [...s].find((x: any): any => x !== "0" && x !== "1") : s[0];
    const minimum = target ? Number(s.replace(new RegExp(target, "g"), s[0] === target ? "1" : "0")) : num;
    return maximum - minimum;
}
