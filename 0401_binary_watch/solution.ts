// LeetCode 0401 - Binary Watch
export function readBinaryWatch(turnedOn: number): string[] {
    const result: string[] = [];
    const bitCount = (value: number) => value.toString(2).split("1").length - 1;
    for (let hour = 0; hour < 12; hour += 1) {
        for (let minute = 0; minute < 60; minute += 1) {
            if (bitCount(hour) + bitCount(minute) === turnedOn) {
                result.push(`${hour}:${String(minute).padStart(2, "0")}`);
            }
        }
    }
    return result;
}
