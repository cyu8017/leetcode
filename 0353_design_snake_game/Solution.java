// LeetCode 0353 - Design Snake Game

// https://leetcode.com/problems/design-snake-game/



import java.util.ArrayDeque;

import java.util.Deque;

import java.util.HashSet;

import java.util.Set;



class SnakeGame {

    private final int width;

    private final int height;

    private final int[][] food;

    private int foodIndex;

    private int score;

    private final Deque<int[]> snake = new ArrayDeque<>();

    private final Set<String> body = new HashSet<>();



    public SnakeGame(int width, int height, int[][] food) {

        this.width = width;

        this.height = height;

        this.food = food;

        this.foodIndex = 0;

        this.score = 0;

        snake.offerFirst(new int[] {0, 0});

        body.add("0,0");

    }



    public int move(String direction) {

        int[] head = snake.peekFirst();

        int row = head[0];

        int col = head[1];



        if ("U".equals(direction)) {

            row--;

        } else if ("D".equals(direction)) {

            row++;

        } else if ("L".equals(direction)) {

            col--;

        } else {

            col++;

        }



        if (row < 0 || row >= height || col < 0 || col >= width) {

            return -1;

        }



        boolean willEat = foodIndex < food.length

            && row == food[foodIndex][0]

            && col == food[foodIndex][1];



        if (!willEat) {

            int[] tail = snake.pollLast();

            body.remove(tail[0] + "," + tail[1]);

        }



        String key = row + "," + col;

        if (body.contains(key)) {

            return -1;

        }



        snake.offerFirst(new int[] {row, col});

        body.add(key);



        if (willEat) {

            score++;

            foodIndex++;

        }



        return score;

    }

}
