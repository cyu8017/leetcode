// LeetCode 0353 - Design Snake Game

// https://leetcode.com/problems/design-snake-game/



using System.Collections.Generic;



public class SnakeGame {

    private readonly int width;

    private readonly int height;

    private readonly int[][] food;

    private int foodIndex;

    private int score;

    private readonly LinkedList<int[]> snake = new();

    private readonly HashSet<string> body = new();



    public SnakeGame(int width, int height, int[][] food) {

        this.width = width;

        this.height = height;

        this.food = food;

        this.foodIndex = 0;

        this.score = 0;

        snake.AddFirst(new int[] {0, 0});

        body.Add("0,0");

    }



    public int Move(string direction) {

        int[] head = snake.First!.Value;

        int row = head[0];

        int col = head[1];



        if (direction == "U") {

            row--;

        } else if (direction == "D") {

            row++;

        } else if (direction == "L") {

            col--;

        } else {

            col++;

        }



        if (row < 0 || row >= height || col < 0 || col >= width) {

            return -1;

        }



        bool willEat = foodIndex < food.Length

            && row == food[foodIndex][0]

            && col == food[foodIndex][1];



        if (!willEat) {

            int[] tail = snake.Last!.Value;

            snake.RemoveLast();

            body.Remove($"{tail[0]},{tail[1]}");

        }



        string key = $"{row},{col}";

        if (body.Contains(key)) {

            return -1;

        }



        snake.AddFirst(new int[] {row, col});

        body.Add(key);



        if (willEat) {

            score++;

            foodIndex++;

        }



        return score;

    }

}
