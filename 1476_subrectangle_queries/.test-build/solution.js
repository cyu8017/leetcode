"use strict";
class SubrectangleQueries {
    constructor(rectangle) {
        this.rectangle = rectangle;
    }
    updateSubrectangle(row1, col1, row2, col2, newValue) {
        for (let row = row1; row <= row2; row++) {
            for (let col = col1; col <= col2; col++)
                this.rectangle[row][col] = newValue;
        }
    }
    getValue(row, col) {
        return this.rectangle[row][col];
    }
}
