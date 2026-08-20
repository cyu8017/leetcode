class SubrectangleQueries {
    rectangle: any;
    constructor(rectangle: any) {

        this.rectangle = rectangle;
    }
    updateSubrectangle(row1: any, col1: any, row2: any, col2: any, newValue: any): any {

        for (let row = row1; row <= row2; row++) {
            for (let col = col1; col <= col2; col++) this.rectangle[row][col] = newValue;
        }
    }
    getValue(row: any, col: any): any {

        return this.rectangle[row][col];
    }
}
