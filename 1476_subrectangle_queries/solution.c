// LeetCode 1476 - Subrectangle Queries
// https://leetcode.com/problems/subrectangle-queries/

#include <stdlib.h>

typedef struct {
    int** rectangle;
    int rows;
    int cols;
} SubrectangleQueries;

SubrectangleQueries* subrectangleQueriesCreate(int** rectangle, int rectangleSize, int* rectangleColSize) {
    SubrectangleQueries* obj = (SubrectangleQueries*)malloc(sizeof(SubrectangleQueries));
    obj->rows = rectangleSize;
    obj->cols = rectangleColSize[0];
    obj->rectangle = (int**)malloc(obj->rows * sizeof(int*));
    for (int r = 0; r < obj->rows; r++) {
        obj->rectangle[r] = (int*)malloc(obj->cols * sizeof(int));
        for (int c = 0; c < obj->cols; c++) obj->rectangle[r][c] = rectangle[r][c];
    }
    return obj;
}

void subrectangleQueriesUpdateSubrectangle(SubrectangleQueries* obj, int row1, int col1, int row2, int col2, int newValue) {
    for (int r = row1; r <= row2; r++)
        for (int c = col1; c <= col2; c++)
            obj->rectangle[r][c] = newValue;
}

int subrectangleQueriesGetValue(SubrectangleQueries* obj, int row, int col) {
    return obj->rectangle[row][col];
}

void subrectangleQueriesFree(SubrectangleQueries* obj) {
    for (int r = 0; r < obj->rows; r++) free(obj->rectangle[r]);
    free(obj->rectangle); free(obj);
}
