function buildArray(target: any, n: any): any {
    const answer: any[] = []; let value = 1;
    for (const wanted of target) { while (value < wanted) { answer.push("Push", "Pop"); value++; } answer.push("Push"); value++; }
    return answer;
}
